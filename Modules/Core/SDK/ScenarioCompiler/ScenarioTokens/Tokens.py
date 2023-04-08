from Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.TokenTypes import STDTokenTypes


class STDLexerTokens:
    TERMINATE_SYMBOLS = ["=", "(", ")", ";", "{", "}", ","]
    WHITESPACE_SYMBOLS = ['\n', '\t', '\r', " "]
    # обычные токены
    TOKENS = {
        'function': STDTokenTypes.FUNC_DEFINITION,
        '(': STDTokenTypes.SUBEXPR_START,
        ')': STDTokenTypes.SUBEXPR_END,
        '{': STDTokenTypes.BODY_START,
        '}': STDTokenTypes.BODY_END,
        ';': STDTokenTypes.ENDLINE,
        '=': STDTokenTypes.ASSIGMENT_OPERATION,
        'loop': STDTokenTypes.SPECIAL_INSTRUCTION,
        ',': STDTokenTypes.ARG_DELIMITER
            }
    # спец токены
    STR_LITERAL_TOKEN = STDTokenTypes.STR_LITERAL
    NUMBER_LITERAL_TOKEN = STDTokenTypes.NUMBER_LITERAL
    OBJECT_TOKEN = STDTokenTypes.OBJECT
    UNDEFINED_TOKEN = STDTokenTypes.UNIDENTIFIED


class STDSyntaxTokens:
    FUNC_DEF = STDTokenTypes.FUNC_DEFINITION
    SUBEXPR_START = STDTokenTypes.SUBEXPR_START
    SUBEXPR_END = STDTokenTypes.SUBEXPR_END
    BODY_START = STDTokenTypes.BODY_START
    BODY_END = STDTokenTypes.BODY_END
    ENDLINE = STDTokenTypes.ENDLINE
    ASSIGMENT_OPERATION = STDTokenTypes.ASSIGMENT_OPERATION
    SPECIAL_INSTRUCTION = STDTokenTypes.SPECIAL_INSTRUCTION
    ARG_DELIMITER = STDTokenTypes.ARG_DELIMITER
    STR_LITERAL = STDTokenTypes.STR_LITERAL
    NUMBER_LITERAL = STDTokenTypes.NUMBER_LITERAL
    OBJECT = STDTokenTypes.OBJECT
    FUNC_CALL = STDTokenTypes.FUNC_CALL
    FUNC_CALL_ARG = STDTokenTypes.FUNC_CALL_ARG
    FUNC_CALL_ARG_LIST = STDTokenTypes.FUNC_CALL_ARG_LIST
    FUNC_DEF_ARG = STDTokenTypes.FUNC_DEF_ARG
    FUNC_DEF_ARG_LIST = STDTokenTypes.FUNC_DEF_ARG_LIST
    LOOP_ARG = STDTokenTypes.LOOP_ARG
    EXPR = STDTokenTypes.EXPR
    UNKNOWN = STDTokenTypes.UNIDENTIFIED
    BODY = STDTokenTypes.BODY
    BODY_LINE = STDTokenTypes.BODY_LINE
    LINE = STDTokenTypes.LINE
    SCENARIO = STDTokenTypes.SCENARIO


class STDLinkerTokens:
    API_FUNC_CALL = STDTokenTypes.API_FUNC_CALL
    USER_FUNC_CALL = STDTokenTypes.USER_FUNC_CALL
    FUNC_CALL = STDTokenTypes.FUNC_CALL
