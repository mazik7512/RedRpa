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

    def _next_pos(self):
        if self._last_scenario_pos < len(self._scenario):
            self._last_scenario_pos += 1

    def _next_char(self):
        if self._last_scenario_pos < len(self._scenario):
            return self._scenario[self._last_scenario_pos]

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
        if not token_value or len(token_value) == 0:
            return None
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
        while self._last_scenario_pos < len(self._scenario):
            cur_char = self._next_char()
            if cur_char in STDLexerTokens.COMMENTARY_SYMBOLS: # для комментариев
                while self._last_scenario_pos < len(self._scenario) and cur_char not in STDLexerTokens.NEW_LINE_SYMBOLS:
                    self._next_pos()
                    cur_char = self._next_char()
                self._next_pos()
            elif cur_char in STDLexerTokens.LITERAL_TERMINATE_SYMBOLS: # для str-литералов
                buffer += cur_char
                self._next_pos()
                cur_char = self._next_char()
                while self._last_scenario_pos < len(self._scenario) and cur_char not in STDLexerTokens.LITERAL_TERMINATE_SYMBOLS:
                    buffer += cur_char
                    self._next_pos()
                    cur_char = self._next_char()
                buffer += cur_char
                self._next_pos()
            elif cur_char not in STDLexerTokens.TERMINATE_SYMBOLS + STDLexerTokens.WHITESPACE_SYMBOLS: # общий случай
                buffer += cur_char
                self._next_pos()
            else:
                break
        if len(buffer) == 0:
            self._next_pos()
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
        self._errors.clear()
        tokens = []
        while self._last_scenario_pos < len(self._scenario):
            token = self.get_next_token()
            if token:
                tokens.append(token)
        work_res = STDWorkResult()
        work_res.push(tokens)
        work_res.push_errors(self._errors)
        return work_res
