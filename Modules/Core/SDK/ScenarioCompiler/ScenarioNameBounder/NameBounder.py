from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioNameBounder.NameBounder import AbstractNameBounder
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDNameResolverTokens
from Modules.Core.SDK.ScenarioExecutable.Sections.ImportsSection import STDImportsSection
from Modules.Core.SDK.ScenarioExecutable.Sections.InitializationSection import STDInitSection
from Modules.Core.Logger.Logger import Logger


MODULE_PREFIX = "[Name Bounder]"


def get_func_calls(func_call_node, api_calls_list, func_calls_list,  func_def_list, api_funcs):
    _type = func_call_node.get_type()
    if _type == STDNameResolverTokens.FUNC_CALL:
        if func_call_node.get_data() in api_funcs:
            api_calls_list.append(func_call_node)
        else:
            func_calls_list.append(func_call_node)
    elif _type == STDNameResolverTokens.FUNC_DEF:
        func_def_list.append(func_call_node.get_data())


class STDRSLNameBounder(AbstractNameBounder):

    def __init__(self, syntax_tree=None, api_funcs_collection=None, logger=Logger):
        self._tree = syntax_tree
        self._stdlib = api_funcs_collection
        self._logger = logger
        self._errors = []

    def set_ast(self, ast):
        self._tree = ast

    def set_apis(self, apis):
        self._stdlib = apis

    def link_names(self):
        api_imports, api_inits = self._link_funcs()
        return api_imports, api_inits

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
        api_imports, api_inits = self._generate_api_sections(api_calls)
        return api_imports, api_inits

    def _generate_api_sections(self, api_calls):
        api_imports = {}
        api_inits = {}
        for func in api_calls:
            api_name = self._stdlib.get_api_name_by_func_name(func.get_data())
            self._generate_import_section(api_name, api_imports)
            self._generate_init_section(api_name, api_inits)
            func.set_data(api_inits[api_name]['api_init_name'] + "." + func.get_data())
        return api_imports, api_inits

    def _link_func_def(self, func_defs, func_calls):
        for func in func_calls:
            if not func.get_data() in func_defs:
                self._error("Неизвесная функция {" + func.get_data() + "}")

    def _generate_import_section(self, api_name, section_data):
        import_string = "from " + self._stdlib.get_api_import_path(api_name) + " import " + api_name
        section_data[api_name] = import_string

    def _generate_init_section(self, api_name, section_data):
        api_init_name = "api_init_" + api_name.lower()
        init_string = api_init_name + " = " + api_name + "()"
        init_section = {'api_init_name': api_init_name, 'api_init': init_string}
        section_data[api_name] = init_section
