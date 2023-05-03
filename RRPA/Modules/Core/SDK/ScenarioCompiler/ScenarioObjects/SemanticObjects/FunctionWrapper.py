from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SemanticObjects.FunctionWrapper import AbstractFunctionWrapper
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSemanticTokens


class STDRSLFunctionWrapper(AbstractFunctionWrapper):

    def __init__(self, func_name, func_args, func_type):
        self._func_name = func_name
        self._func_args = func_args
        self._func_type = func_type

    def get_func_name(self):
        return self._func_name

    def get_func_args_count(self):
        return len(self._func_args)

    def get_func_args_types(self):
        arg_types = []
        for arg in self._func_args:
            arg_type = self._get_arg_type(arg)
            arg_types.append(arg_type)
        return arg_types

    def get_func_arg_type(self, index):
        return self._get_arg_type(self._func_args[index])

    def get_func_type(self):
        return self._func_type

    def _get_arg_type(self, arg):
        arg_data = arg.split(":")
        arg_type = arg_data[1].strip()
        if arg_type == "str":
            return STDSemanticTokens.STR_LITERAL_TYPE
        elif arg_type == "int":
            return STDSemanticTokens.NUMBER_LITERAL_TYPE
        else:
            return STDSemanticTokens.ANY_TYPE
