from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.TranslatorPolicies.TranslationPolicy import \
    AbstractTranslationPolicy
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSyntaxTokens
from RRPA.Modules.Core.Policies.CompilerPolicies.TranslatorPolicies.NameTranslationPolicy import \
    STDRSLNameTranslationPolicy
from RRPA.Modules.Core.Policies.CompilerPolicies.TranslatorPolicies.OffsetTranslationPolicy import \
    STDRSLOffsetTranslationPolicy


class STDRSLTranslationPolicy(AbstractTranslationPolicy):
    name_translation_policy = STDRSLNameTranslationPolicy
    offset_policy = STDRSLOffsetTranslationPolicy

    @staticmethod
    def translate_expr(node):
        result_init, result = node.get_left_node().deserialize()
        res = result_init + result
        return res

    @staticmethod
    def translate_loop(node):
        result = ""
        loop_header_init, loop_header = node.get_left_node().deserialize()
        loop_body = node.get_right_node().deserialize()
        if len(loop_header_init) > 0:
            loop_header_init += '\n' + STDRSLTranslationPolicy.offset_policy.get_current_offset()
        result += loop_header_init + "for " + loop_header + ":\n" + loop_body
        return result

    @staticmethod
    def translate_loop_header(node):
        loop_arg_name = STDRSLTranslationPolicy.name_translation_policy.generate_loop_arg_name()
        loop_data_name = STDRSLTranslationPolicy.name_translation_policy.generate_loop_data_name()
        loop_arg_init = ""
        loop_arg_data = ""
        loop_arg_node = node.get_left_node()
        if loop_arg_node.get_type() == STDSyntaxTokens.FUNC_CALL:
            loop_arg_init, loop_arg_data = loop_arg_node.deserialize()
            loop_arg_init += loop_data_name + " = " + loop_arg_data
            loop_arg_data = loop_data_name
        else:
            loop_arg_data = loop_arg_node.deserialize()
        result = loop_arg_name + " in range(1, " + loop_arg_data + ")"
        return loop_arg_init, result

    @staticmethod
    def translate_return(node):
        result = ""
        return_init = ""
        return_data = "return "
        _return_data = ""
        return_arg_node = node.get_left_node()
        if return_arg_node:
            return_init, _return_data = return_arg_node.deserialize()
        if "=" in return_init:
            return_init += "\n" + STDRSLTranslationPolicy.offset_policy.get_current_offset()
        return_data += _return_data
        result += return_init + return_data
        return result

    @staticmethod
    def translate_return_arg(node):
        result_init, result = STDRSLTranslationPolicy._translate_standart_call_arg(node)
        return result_init, result

    @staticmethod
    def translate_func_def(node):
        func_def_args = node.get_left_node()
        if func_def_args:
            func_def_args = func_def_args.deserialize()
        else:
            func_def_args = ""
        result = "def " + node.get_data() + "(" + func_def_args + "):\n"
        func_def_body = node.get_right_node().deserialize()
        result += func_def_body + "\n"
        return result

    @staticmethod
    def translate_func_def_arg_list(node):
        result = ""
        arg = node.get_left_node()
        if arg:
            result += arg.deserialize()
            other_args = node.get_right_node()
            if other_args:
                result += ", "
                result += other_args.deserialize()
        return result

    @staticmethod
    def translate_func_def_arg(node):
        result = node.get_left_node().deserialize()
        return result

    @staticmethod
    def translate_func_call(node):
        func_args = node.get_left_node()
        call_args_init = ""
        call_args = ""
        if func_args:
            call_args_init, call_args = func_args.deserialize()
        result_init = call_args_init
        result = node.get_data() + "(" + call_args + ")"
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
                result_init += arg_init + "\n"
                result += ", " + arg
        return result_init, result

    @staticmethod
    def translate_func_call_arg(node):
        result_init, result = STDRSLTranslationPolicy._translate_standart_call_arg(node)
        return result_init, result

    @staticmethod
    def _translate_standart_call_arg(node):
        result_init = ""
        result = ""
        arg = node.get_left_node()
        if not arg:
            return result_init, result
        if arg.get_type() == STDSyntaxTokens.FUNC_CALL:
            func_arg_init, func_arg = arg.deserialize()
            func_arg_name = STDRSLTranslationPolicy.name_translation_policy.generate_func_call_arg_name()
            if len(func_arg_init) > 0:
                result_init += STDRSLTranslationPolicy.offset_policy.get_current_offset() + func_arg_init + "\n"
            result_init += func_arg_name + " = " + func_arg
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
        elif rvalue.get_type() == STDSyntaxTokens.ASSIGMENT_OPERATION:
            result_init, _result = rvalue.deserialize()
        else:
            _result += rvalue.deserialize()
        lvalue = node.get_right_node().deserialize()
        result += lvalue + " " + node.get_data() + " " + _result
        return result_init, result

    @staticmethod
    def translate_body(node):
        STDRSLTranslationPolicy.offset_policy.add_offset_level()
        result = node.get_left_node().deserialize()
        if result == "":
            result = STDRSLTranslationPolicy.offset_policy.get_current_offset() + "pass"
        STDRSLTranslationPolicy.offset_policy.remove_offset_level()
        return result

    @staticmethod
    def translate_body_line(node):
        offset = STDRSLTranslationPolicy.offset_policy.get_current_offset()
        result = ""
        line_expr = node.get_left_node()
        if line_expr:
            result += offset + line_expr.deserialize()
            if not result.endswith("\n"):
                result += "\n"
            next_line = node.get_right_node().deserialize()
            result += next_line
        return result

    @staticmethod
    def translate_line(node):
        result = ""
        line = node.get_left_node().deserialize()
        result += line
        if not result.endswith('\n'):
            result += '\n'
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
