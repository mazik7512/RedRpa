from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNode import STDRSLSyntaxNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSyntaxTokens
from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.TranslatorPolicies.TranslationPolicy import \
    AbstractTranslationPolicy
from RRPA.Modules.Core.Policies.CompilerPolicies.TranslatorPolicies.TranslationPolicy import STDRSLTranslationPolicy


class STDRSLObjectNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.OBJECT, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_object(self)


class STDRSLStrLiteralNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.STR_LITERAL, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_str_literal(self)


class STDRSLNumberLiteralNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.NUMBER_LITERAL, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_number_literal(self)


class STDRSLFuncDefNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.FUNC_DEF, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_func_def(self)


class STDRSLFuncDefArgListNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.FUNC_DEF_ARG_LIST, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_func_def_arg_list(self)


class STDRSLFuncDefArgNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.FUNC_DEF_ARG, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_func_def_arg(self)


class STDRSLLoopNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.SPECIAL_INSTRUCTION, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_loop(self)


class STDRSLLoopHeaderNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.LOOP_ARG, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_loop_header(self)


class STDRSLBodyNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.BODY, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_body(self)


class STDRSLBodyLineNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.BODY_LINE, data)
        self._policy = translation_policy

    def deserialize(self, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        return self._policy.translate_body_line(self)


class STDRSLFuncCallNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.FUNC_CALL, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_func_call(self)


class STDRSLFuncCallArgListNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.FUNC_CALL_ARG_LIST, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_func_call_arg_list(self)


class STDRSLFuncCallArgNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.FUNC_CALL_ARG, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_func_call_arg(self)


class STDRSLAssigmentNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.ASSIGMENT_OPERATION, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_assigment(self)


class STDRSLExprNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.EXPR, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_expr(self)


class STDRSLLineNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.LINE, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_line(self)


class STDRSLScenarioNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.SCENARIO, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_scenario(self)


class STDRSLReturnNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.SPECIAL_INSTRUCTION, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_return(self)


class STDRSLReturnArgNode(STDRSLSyntaxNode):

    def __init__(self, data, translation_policy: AbstractTranslationPolicy = STDRSLTranslationPolicy):
        super().__init__(STDSyntaxTokens.RETURN_ARG, data)
        self._policy = translation_policy

    def deserialize(self):
        return self._policy.translate_return_arg(self)
