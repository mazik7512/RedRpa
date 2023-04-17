from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.LexicalObjects.Lexeme import AbstractLexema


class STDLexema(AbstractLexema):

    def __init__(self, token_type, token_val):
        super().__init__(token_type, token_val)
