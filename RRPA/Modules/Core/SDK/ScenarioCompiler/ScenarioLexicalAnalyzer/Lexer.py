from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.LexicalAnalyzer.Lexer import AbstractLexer
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDLexerTokens
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.LexicalObjects.Lexeme import STDLexema
from RRPA.Modules.Core.General.DataStructures.WorkResult import STDWorkResult
from RRPA.Modules.Core.Logger.Logger import Logger


class STDRSLLexer(AbstractLexer):

    def __init__(self, scenario=None, logger=Logger):
        self._logger = logger
        self._scenario = scenario
        self._last_scenario_pos = 0
        self._errors = []

    def _prepare_scenario_text(self, data):
        if data:
            return data.strip()
        return data

    def set_data(self, data):
        self._errors.clear()
        self._scenario = self._prepare_scenario_text(data)
        self._last_scenario_pos = 0

    def __str_literal_check(self, token_value: str):
        if token_value.startswith("\"") and token_value.endswith("\""):
            return True
        else:
            return False

    def __number_literal_check(self, token_value: str):
        result = True if token_value[0] == '-' or token_value[0].isdigit() else False
        if not result:
            return False
        have_point = False
        for i in range(1, len(token_value) - 1):
            if token_value[i].isdigit():
                pass
            elif token_value[i] == "." and not have_point:
                have_point = True
            else:
                return False
        return True

    def __literal_check(self, token_value: str):
        if self.__str_literal_check(token_value):
            return STDLexema(STDLexerTokens.STR_LITERAL_TOKEN, token_value)
        elif self.__number_literal_check(token_value):
            return STDLexema(STDLexerTokens.NUMBER_LITERAL_TOKEN, token_value)
        else:
            return None

    def __specify_token_type(self, token_value: str):
        _type = STDLexerTokens.UNDEFINED_TOKEN
        if token_value in STDLexerTokens.TOKENS:
            _type = STDLexerTokens.TOKENS[token_value]
            token_object = STDLexema(_type, token_value)
        else:
            token_object = self.__literal_check(token_value)
            if not token_object:
                token_object = STDLexema(STDLexerTokens.OBJECT_TOKEN, token_value)
        return token_object

    def __get_token_value(self):
        buffer = ""
        cur_char = ""
        commentary = ""
        while self._last_scenario_pos < len(self._scenario):
            cur_char = self._scenario[self._last_scenario_pos]
            if cur_char in STDLexerTokens.COMMENTARY_SYMBOLS:
                while self._last_scenario_pos < len(self._scenario) and cur_char not in STDLexerTokens.NEW_LINE_SYMBOLS:
                    commentary += cur_char
                    self._last_scenario_pos += 1
                    cur_char = self._scenario[self._last_scenario_pos]
                self._last_scenario_pos += 1
            elif cur_char not in STDLexerTokens.TERMINATE_SYMBOLS + STDLexerTokens.WHITESPACE_SYMBOLS:
                buffer += cur_char
                self._last_scenario_pos += 1
            else:
                break
        if len(buffer) == 0:
            self._last_scenario_pos += 1
            return cur_char
        else:
            return buffer

    def get_next_token(self):
        token_value = self.__get_token_value()
        if token_value in STDLexerTokens.WHITESPACE_SYMBOLS:
            return self.get_next_token()
        token_object = self.__specify_token_type(token_value)
        return token_object

    def get_token_list(self):
        tokens = []
        while self._last_scenario_pos < len(self._scenario):
            tokens.append(self.get_next_token())
        work_res = STDWorkResult()
        work_res.push(tokens)
        work_res.push_errors(self._errors)
        return work_res
