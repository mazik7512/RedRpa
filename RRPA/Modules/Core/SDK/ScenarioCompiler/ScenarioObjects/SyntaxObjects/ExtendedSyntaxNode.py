from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNode import STDRSLSyntaxNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSyntaxTokens
from RRPA.Modules.Core.Policies.CompilerPolicies.TranslatorPolicies.TranslationPolicy import STDRSLTranslationPolicy


class STDRSLObjectNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.OBJECT, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_object(self)


class STDRSLStrLiteralNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.STR_LITERAL, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_str_literal(self)


class STDRSLNumberLiteralNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.NUMBER_LITERAL, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_number_literal(self)


class STDRSLFuncDefNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_DEF, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_func_def(self)


class STDRSLFuncDefArgListNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_DEF_ARG_LIST, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_func_def_arg_list(self)


class STDRSLFuncDefArgNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_DEF_ARG, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_func_def_arg(self)


class STDRSLLoopNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.SPECIAL_INSTRUCTION, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_loop(self)


class STDRSLLoopHeaderNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.LOOP_ARG, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_loop_header(self)


class STDRSLBodyNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.BODY, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_body(self)


class STDRSLBodyLineNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.BODY_LINE, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_body_line(self)


class STDRSLFuncCallNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_CALL, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_func_call(self)


class STDRSLFuncCallArgListNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_CALL_ARG_LIST, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_func_call_arg_list(self)


class STDRSLFuncCallArgNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.FUNC_CALL_ARG, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_func_call_arg(self)


class STDRSLAssigmentNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.ASSIGMENT_OPERATION, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_assigment(self)


class STDRSLExprNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.EXPR, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_expr(self)


class STDRSLLineNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.LINE, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_line(self)


class STDRSLScenarioNode(STDRSLSyntaxNode):

    def __init__(self, data):
        super().__init__(STDSyntaxTokens.SCENARIO, data)

    def deserialize(self):
        return STDRSLTranslationPolicy.translate_scenario(self)
