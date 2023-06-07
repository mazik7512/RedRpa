from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioNameBounding.NameBounder import AbstractNameBounder
from RRPA.Modules.Core.Policies.CompilerPolicies.NameBoundingPolicies.ImportPolicy import STDImportPolicy
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDNameBounderTokens
from RRPA.Modules.Core.Logger.Logger import Logger
from RRPA.Modules.Core.General.DataStructures.WorkResult import STDWorkResult

MODULE_PREFIX = "[Name Bounder]"


def get_func_calls(func_call_node, api_calls_list, func_calls_list, func_def_list, api_funcs):
    _type = func_call_node.get_type()
    if _type == STDNameBounderTokens.FUNC_CALL:
        if func_call_node.get_data() in api_funcs:
            api_calls_list.append(func_call_node)
        else:
            func_calls_list.append(func_call_node)
    elif _type == STDNameBounderTokens.FUNC_DEF:
        func_def_list.append(func_call_node.get_data())


class STDRSLNameBounder(AbstractNameBounder):

    def __init__(self, syntax_tree=None, api_collector=None, tools=None, import_policy=STDImportPolicy, logger=Logger):
        # self._os_utils = tools['os']
        # self._web_utils = tools['web']
        self._tools = tools
        self._tree = syntax_tree
        self._stdlib = api_collector
        self._import_policy = import_policy
        self._logger = logger
        self._errors = []

    def set_ast(self, ast):
        self._tree = ast

    def set_apis(self, apis):
        self._stdlib = apis

    def link_names(self):
        self._errors.clear()
        tools_imports, tools_inits, api_imports, api_inits = self._link_funcs()
        work_res = STDWorkResult()
        work_res.push(({'tools': tools_imports, 'api': api_imports},
                       {'tools:': tools_inits, 'api': api_inits}))
        work_res.push_errors(self._errors)
        return work_res

    def _error(self, error_data):
        self._logger.error(MODULE_PREFIX, "Ошибка связывания имён:", error_data)
        self._errors.append(error_data)

    def _link_funcs(self):
        func_calls = []
        api_calls = []
        func_defs = []
        api_functions = self._stdlib.get_all_api_methods()
        self._tree.traverse("preorder", get_func_calls, api_calls, func_calls, func_defs, api_functions)
        self._link_func_def(func_defs, func_calls)
        tools_import, tools_init, api_imports, api_inits = self._generate_api_sections(api_calls)
        return tools_import, tools_init, api_imports, api_inits

    def _generate_tools(self, section_data):
        keys = self._tools.keys()
        for key in keys:
            section_data[key] = self._import_policy.generate_import(self._tools[key].get_tools_name())

    def _generate_api_sections(self, api_calls):
        api_imports = {}
        api_inits = {}
        tools_imports = {}
        tools_inits = {}
        self._generate_tools(tools_imports)
        tools_init_name = self._generate_tools_init_section(tools_inits)
        for func in api_calls:
            api_name = self._stdlib.get_api_name_by_func_name(func.get_data())
            self._generate_import_section(api_name, api_imports)
            self._generate_api_init_section(api_name, tools_init_name, api_inits)
            func.set_data(api_inits[api_name]['init_name'] + "." + func.get_data())
        return tools_imports, tools_inits, api_imports, api_inits

    def _link_func_def(self, func_defs, func_calls):
        for func in func_calls:
            if not func.get_data() in func_defs:
                self._error("Неизвестная функция {" + func.get_data() + "}")

    def _generate_import_section(self, api_name, section_data):
        import_string = self._import_policy.generate_import(api_name)
        section_data[api_name] = import_string

    def _generate_api_init_section(self, api_name, tools_name, section_data):
        api_init_name = "api_init_" + api_name.lower()
        init_string = api_init_name + " = " + api_name + "({})".format(tools_name)
        init_section = {'init_name': api_init_name, 'init_code': init_string}
        section_data[api_name] = init_section

    def _generate_tools_init_section(self, section_data):
        tools_init_name = "tools_init"
        init_string = tools_init_name + " = " + "{'os': " + self._tools['os'].get_tools_name() + \
                      ", 'web': " + self._tools['web'].get_tools_name() + "}"
        init_section = {'init_name': tools_init_name, 'init_code': init_string}
        section_data['tools_init'] = init_section
        return tools_init_name
