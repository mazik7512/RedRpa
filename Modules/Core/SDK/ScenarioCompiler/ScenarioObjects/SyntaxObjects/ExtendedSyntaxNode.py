from Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNode import STDRSLSyntaxNode
from Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSyntaxTokens


class STDRSLObjectNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.OBJECT, data)

    def deserialize(self):
        return self.get_data()


class STDRSLStrLiteralNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.STR_LITERAL, data)

    def deserialize(self):
        return self.get_data()


class STDRSLNumberLiteralNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.NUMBER_LITERAL, data)

    def deserialize(self):
        return self.get_data()


class STDRSLFuncDefNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_DEF, data)

    def deserialize(self):
        func_def_args = self.get_left_node().deserialize()
        result = "def " + self.get_data() + func_def_args + ":\n"
        func_def_body = self.get_right_node().deserialize()
        result += func_def_body
        return result


class STDRSLFuncDefArgListNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_DEF_ARG_LIST, data)

    def deserialize(self):
        result = "("
        arg = self.get_left_node()
        if arg:
            result += arg.deserialize()
            other_args = self.get_right_node()
            if other_args:
                result += ","
                result += other_args.deserialize()
        result += ")"
        return result


class STDRSLFuncDefArgNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_DEF_ARG, data)

    def deserialize(self):
        result = self.get_left_node().deserialize()
        return result


class STDRSLFuncDefBody(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.BODY, data)

    def deserialize(self):
        result = self.get_left_node().deserialize()
        return result


class STDRSLLoopNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.SPECIAL_INSTRUCTION, data)

    def deserialize(self):
        result = "for "
        loop_header = self.get_left_node().deserialize()
        loop_body = self.get_right_node().deserialize()
        result += loop_header + ":\n" + loop_body
        return result


class STDRSLLoopHeaderNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.LOOP_ARG, data)

    def deserialize(self):
        loop_arg_name = "loop_arg "
        result = loop_arg_name + "in range(0, " + self.get_left_node().deserialize() + ")"
        return result


class STDRSLLoopBodyNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.BODY, data)

    def deserialize(self):
        result = self.get_left_node().deserialize()
        return result


class STDRSLBodyNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.BODY, data)

    def deserialize(self):
        result = self.get_left_node().deserialize()
        return result


class STDRSLBodyLineNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.BODY_LINE, data)

    def deserialize(self):
        offset = "\t"
        result = ""
        line_expr = self.get_left_node().deserialize()
        result += offset + line_expr + "\n"
        next_line = self.get_right_node().deserialize()
        result += next_line
        return result


class STDRSLFuncCallNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_CALL, data)

    def deserialize(self):
        call_args_init, call_args = self.get_left_node().deserialize()
        result_init = call_args_init
        result = self.get_data() + "(" +call_args + ")\n"
        return result_init, result


class STDRSLFuncCallArgListNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_CALL_ARG_LIST, data)

    def deserialize(self):
        result_init = ""
        result = ""
        func_arg = self.get_left_node()
        if func_arg:
            arg_init, arg = func_arg.deserialize()
            result_init += arg_init
            result += arg
            other_args = self.get_right_node()
            if other_args:
                arg_init, arg = other_args.deserialize()
                result_init += + arg_init + "\n"
                result += "," + arg
        return result_init, result


class STDRSLFuncCallArgNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_CALL_ARG, data)

    def deserialize(self):
        result_init = ""
        result = ""
        arg = self.get_left_node()
        if arg.get_type() == STDSyntaxTokens.FUNC_CALL:
            func_arg_init, func_arg = arg.deserialize()
            result_init += func_arg_init + "\n" + "func_arg = " + func_arg
            result += func_arg
        else:
            result += arg.deserialize()
        return result_init, result


class STDRSLAssigmentNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.ASSIGMENT_OPERATION, data)

    def deserialize(self):
        result_init = ""
        result = ""
        _result = ""
        rvalue = self.get_left_node()
        if rvalue.get_type() == STDSyntaxTokens.FUNC_CALL:
            result_init, _result = rvalue.deserialize()
        else:
            _result += rvalue.deserialize()
        lvalue = self.get_right_node().deserialize()
        result += lvalue + " " + self.get_data() + " " + _result
        return result_init, result


class STDRSLExprNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.EXPR, data)

    def deserialize(self):
        result_init, result = self.get_left_node().deserialize()
        res = result_init + "\n" + result
        return res


class STDRSLLineNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.LINE, data)

    def deserialize(self):
        result = ""
        line = self.get_left_node().deserialize()
        result += line + "\n"
        next_line = self.get_right_node()
        if next_line:
            result += next_line.deserialize()
        return result


class STDRSLScenarioNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.SCENARIO, data)

    def deserialize(self):
        result = self.get_left_node().deserialize()
        return result
