from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.CompileErrorsProcessingPolicy import AbstractCompileErrorsProcessingPolicy
from RRPA.Modules.Core.Exceptions.Exceptions import STDLexicalException
from RRPA.Modules.Core.Exceptions.Exceptions import STDSyntaxException
from RRPA.Modules.Core.Exceptions.Exceptions import STDNameBoundException
from RRPA.Modules.Core.Exceptions.Exceptions import STDTranslationException


class STDCompileErrorsProcessingPolicy(AbstractCompileErrorsProcessingPolicy):

    @staticmethod
    def process_errors(errors_type, errors):
        if len(errors) > 0:
            errors_processor_name = "_process_" + errors_type + "_errors"
            errors_processor = getattr(STDCompileErrorsProcessingPolicy, errors_processor_name)
            errors_processor(errors)

    @staticmethod
    def _process_lex_errors(errors):
        lex_exception = STDLexicalException(errors)
        raise lex_exception

    @staticmethod
    def _process_syntax_errors(errors):
        syntax_exception = STDSyntaxException(errors)
        raise syntax_exception

    @staticmethod
    def _process_name_bounding_errors(errors):
        name_bounding_exception = STDNameBoundException(errors)
        raise name_bounding_exception

    @staticmethod
    def _process_translation_errors(errors):
        translation_exception = STDTranslationException()
        raise translation_exception
