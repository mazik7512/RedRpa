from Modules.Core.Abstract.Policies.CompilerPolicies.TranslatorPolicies.TranslationPolicy import AbstractTranslationPolicy
from Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSyntaxTokens
from Modules.Core.Policies.CompilerPolicies.TranslatorPolicies.NameTranslationPolicy import STDRSLNameTranslationPolicy


class STDRSLTranslationPolicy(AbstractTranslationPolicy):

    @staticmethod
    def translate_expr(node):
        result_init, result = node.get_left_node().deserialize()
        res = result_init + "\n" + result
        return res

    @staticmethod
    def translate_loop(node):
        result = "for "
        loop_header = node.get_left_node().deserialize()
        loop_body = node.get_right_node().deserialize()
        result += loop_header + ":\n" + loop_body
        return result

    @staticmethod
    def translate_loop_header(node):
        loop_arg_name = STDRSLNameTranslationPolicy.generate_loop_arg_name()
        result = loop_arg_name + " in range(1, " + node.get_left_node().deserialize() + "):"
        return result

    @staticmethod
    def translate_func_def(node):
        func_def_args = node.get_left_node().deserialize()
        result = "def " + node.get_data() + func_def_args + ":\n"
        func_def_body = node.get_right_node().deserialize()
        result += func_def_body
        return result

    @staticmethod
    def translate_func_def_arg_list(node):
        result = "("
        arg = node.get_left_node()
        if arg:
            result += arg.deserialize()
            other_args = node.get_right_node()
            if other_args:
                result += ","
                result += other_args.deserialize()
        result += ")"
        return result

    @staticmethod
    def translate_func_def_arg(node):
        result = node.get_left_node().deserialize()
        return result

    @staticmethod
    def translate_func_call(node):
        call_args_init, call_args = node.get_left_node().deserialize()
        result_init = call_args_init
        result = node.get_data() + "(" + call_args + ")\n"
        return result_init, result

    @staticmethod
    def translate_func_call_arg_list(node):
        result_init = ""
        result = ""
        func_arg = node.get_left_node()
        if func_arg:
            arg_init, arg = func_arg.deserialize()
            result_init += arg_init
            result += arg
            other_args = node.get_right_node()
            if other_args:
                arg_init, arg = other_args.deserialize()
                result_init += + arg_init + "\n"
                result += "," + arg
        return result_init, result

    @staticmethod
    def translate_func_call_arg(node):
        result_init = ""
        result = ""
        arg = node.get_left_node()
        if arg.get_type() == STDSyntaxTokens.FUNC_CALL:
            func_arg_init, func_arg = arg.deserialize()
            func_arg_name = STDRSLNameTranslationPolicy.generate_func_call_arg_name()
            result_init += func_arg_init + "\n" + func_arg_name + " = " + func_arg
            result += func_arg_name
        else:
            result += arg.deserialize()
        return result_init, result

    @staticmethod
    def translate_assigment(node):
        result_init = ""
        result = ""
        _result = ""
        rvalue = node.get_left_node()
        if rvalue.get_type() == STDSyntaxTokens.FUNC_CALL:
            result_init, _result = rvalue.deserialize()
        else:
            _result += rvalue.deserialize()
        lvalue = node.get_right_node().deserialize()
        result += lvalue + " " + node.get_data() + " " + _result
        return result_init, result

    @staticmethod
    def translate_body(node):
        result = node.get_left_node().deserialize()
        return result

    @staticmethod
    def translate_body_line(node):
        offset = "\t"
        result = ""
        line_expr = node.get_left_node().deserialize()
        result += offset + line_expr + "\n"
        next_line = node.get_right_node().deserialize()
        result += next_line
        return result

    @staticmethod
    def translate_line(node):
        result = ""
        line = node.get_left_node().deserialize()
        result += line + "\n"
        next_line = node.get_right_node()
        if next_line:
            result += next_line.deserialize()
        return result

    @staticmethod
    def translate_scenario(node):
        result = node.get_left_node().deserialize()
        return result

    @staticmethod
    def translate_object(node):
        result = node.get_data()
        return result

    @staticmethod
    def translate_str_literal(node):
        result = node.get_data()
        return result

    @staticmethod
    def translate_number_literal(node):
        result = node.get_data()
        return result
