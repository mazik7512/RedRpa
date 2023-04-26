from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.TranslatorPolicies.NameTranslationPolicy import AbstractNameTranslationPolicy


class STDRSLNameTranslationPolicy(AbstractNameTranslationPolicy):

    _loop_arg_counter = 0
    _call_args_counter = 0
    _loop_data_counter = 0

    @staticmethod
    def generate_loop_arg_name(*args):
        result = "loop_arg_" + str(STDRSLNameTranslationPolicy._loop_arg_counter)
        STDRSLNameTranslationPolicy._loop_arg_counter += 1
        return result

    @staticmethod
    def generate_func_call_arg_name(*args):
        result = "call_arg_" + str(STDRSLNameTranslationPolicy._call_args_counter)
        STDRSLNameTranslationPolicy._call_args_counter += 1
        return result

    @staticmethod
    def generate_loop_data_name(*args):
        result = "loop_data_" + str(STDRSLNameTranslationPolicy._loop_data_counter)
        STDRSLNameTranslationPolicy._loop_data_counter += 1
        return result
