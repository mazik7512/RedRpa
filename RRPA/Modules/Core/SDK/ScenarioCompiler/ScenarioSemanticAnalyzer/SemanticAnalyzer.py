from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioSemanticAnalyzer.SemanticAnalyzer import \
    AbstractSemanticAnalyzer
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SemanticObjects.FunctionWrapper import STDRSLFunctionWrapper
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTreeIterator import \
    STDRSLPreOrderSyntaxTreeIterator
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSemanticTokens
from RRPA.Modules.Core.General.DataStructures.WorkResult import STDWorkResult
from RRPA.Modules.Core.Logger.Logger import Logger

MODULE_PREFIX = "[Semantic Analyzer]"


def get_function_definition_args(arg_node, arg_counter):
    _type = arg_node.get_type()
    if _type == STDSemanticTokens.FUNC_DEF_ARG_LIST:
        arg_counter[0] += 1


def get_functions_definitions(func_node, tree_iter, functions_list):
    _type = func_node.get_type()
    arg_counter = [0]
    if _type == STDSemanticTokens.FUNC_DEF:
        tree_iter.traverse(func_node.get_left_node(), get_function_definition_args, arg_counter)
        function_wrapper = STDRSLFunctionWrapper(func_node.get_data(), range(arg_counter[0]),
                                                 STDSemanticTokens.USER_FUNC)
        functions_list.append(function_wrapper)


def get_function_call_args(arg_node, args_list):
    if not arg_node:
        return
    _type = arg_node.get_type()
    if _type == STDSemanticTokens.FUNC_CALL_ARG_LIST:
        _arg_node = arg_node.get_left_node().get_left_node()
        arg_name = "arg: "
        arg_type = "str" if _arg_node.get_type() == STDSemanticTokens.STR_LITERAL_TYPE \
            else "int"
        args_list.append(arg_name + arg_type)
        get_function_call_args(arg_node.get_right_node(), args_list)


def get_functions_calls(func_node, functions_list, api_functions_list):
    _type = func_node.get_type()
    if _type == STDSemanticTokens.FUNC_CALL:
        func_args = []
        get_function_call_args(func_node.get_left_node(), func_args)
        func_type = STDSemanticTokens.API_FUNC if func_node.get_data() in api_functions_list \
            else STDSemanticTokens.USER_FUNC
        function_wrapper = STDRSLFunctionWrapper(func_node.get_data(), func_args, func_type)
        functions_list.append(function_wrapper)


class STDRSLSemanticAnalyzer(AbstractSemanticAnalyzer):

    def __init__(self, ast=None, stdlib=None, logger=Logger):
        self._ast = ast
        self._stdlib = stdlib
        self._logger = logger
        self._errors = []

    def set_ast(self, ast):
        self._ast = ast

    def set_stdlib(self, stdlib):
        self._stdlib = stdlib

    def analyze(self):
        self._errors.clear()
        func_defs_list = []
        func_calls_list = []
        tree_iterator = STDRSLPreOrderSyntaxTreeIterator(self._ast)
        api_func_list = self._stdlib.get_all_api_methods()
        self._ast.traverse("preorder", get_functions_definitions, tree_iterator, func_defs_list)
        self._ast.traverse("preorder", get_functions_calls, func_calls_list, api_func_list)
        self._analyze(func_defs_list, func_calls_list, api_func_list)
        result = STDWorkResult()
        result.push_errors(self._errors)
        return result

    def _analyze(self, func_defs_list, func_calls_list, api_functions_list):
        no_duplicates = self._analyze_func_defs_names(func_defs_list, api_functions_list)
        if not no_duplicates:
            return
        api_funcs = self._api_funcs_to_funcs_wrappers(api_functions_list)
        for func_call in func_calls_list:
            func_call_type = func_call.get_func_type()
            if func_call_type == STDSemanticTokens.API_FUNC:
                self._analyze_api_func(func_call, api_funcs)
            elif func_call_type == STDSemanticTokens.USER_FUNC:
                self._analyze_user_func(func_call, func_defs_list)

    def _analyze_func_defs_names(self, func_defs_list, api_func_list):
        used_names = []
        no_errors = True
        for func_def in func_defs_list:
            func_def_name = func_def.get_func_name()
            if func_def_name in used_names:
                self._error("Найдено переопределение функции [{}], манглирование имён не поддерживается".format(func_def_name))
                no_errors = False
            if func_def_name in api_func_list:
                self._error("[{}] Переопределние функций стандартной библиотеки запрещено.".format(func_def_name))
                no_errors = False
            if func_def_name in STDSemanticTokens.KEYWORDS:
                self._error("В имени функции [{}] использовано ключевое слово".format(func_def_name))
                no_errors = False
            used_names.append(func_def_name)
        return no_errors

    def _analyze_api_func(self, func, api_funcs):
        for api_func in api_funcs:
            if api_func.get_func_name() == func.get_func_name():
                self._api_func_analyze(func, api_func)

    def _api_func_analyze(self, func, api_func):
        de_jure_args_count = api_func.get_func_args_count()
        de_facto_args_count = func.get_func_args_count()
        word_ending = self._get_word_ending_by_number(de_jure_args_count)
        if de_jure_args_count != de_facto_args_count:
            self._error("[{}] Требуется {} аргумент{}, а пришло {}".format(func.get_func_name(),
                                                                           de_jure_args_count,
                                                                           word_ending,
                                                                           de_facto_args_count))
            return
        de_jure_args_types = api_func.get_func_args_types()
        de_facto_args_types = func.get_func_args_types()
        for i in range(len(de_jure_args_types)):
            if de_jure_args_types[i] != de_facto_args_types[i] and de_jure_args_types[i] != STDSemanticTokens.ANY_TYPE:
                de_jure_arg_type = "строка или объект" if de_jure_args_types[i] == STDSemanticTokens.STR_LITERAL_TYPE \
                    else "число или объект"
                de_facto_arg_type = "строка" if de_facto_args_types[i] == STDSemanticTokens.STR_LITERAL_TYPE \
                    else "число"
                self._error("[{}] Неверный тип {} аргумента, ожидалась {}, а пришло {}".format(func.get_func_name(),
                                                                                               str(i + 1),
                                                                                               de_jure_arg_type,
                                                                                               de_facto_arg_type))

    def _analyze_user_func(self, func, func_defs):
        for user_func in func_defs:
            if user_func.get_func_name() == func.get_func_name():
                self._user_func_analyze(func, user_func)

    def _user_func_analyze(self, func, func_def):
        de_jure_args_count = func_def.get_func_args_count()
        de_facto_args_count = func.get_func_args_count()
        word_ending = self._get_word_ending_by_number(de_jure_args_count)
        if de_jure_args_count != de_facto_args_count:
            self._error("[{}] Требуется {} аргумент{}, а пришло {}".format(func.get_func_name(),
                                                                           de_jure_args_count,
                                                                           word_ending,
                                                                           de_facto_args_count))

    def _get_word_ending_by_number(self, number):
        if number in (11, 12, 13, 14):
            return "ов"
        elif number % 10 == 1:
            return ""
        elif number % 10 in (2, 3, 4):
            return "a"
        else:
            return "ов"

    def _api_funcs_to_funcs_wrappers(self, api_functions_list):
        api_wrappers = []
        for func in api_functions_list:
            func_wrapper = STDRSLFunctionWrapper(func, self._stdlib.get_func_params_by_func_name(func),
                                                 STDSemanticTokens.API_FUNC)
            api_wrappers.append(func_wrapper)
        return api_wrappers

    def _error(self, error_data):
        self._errors.append(error_data)
        self._logger.error(MODULE_PREFIX, "Семантическая ошибка:", error_data)

    def __parse_arg_type(self, arg_data):
        arg_data = arg_data.split(":")
        return arg_data[1].strip()
