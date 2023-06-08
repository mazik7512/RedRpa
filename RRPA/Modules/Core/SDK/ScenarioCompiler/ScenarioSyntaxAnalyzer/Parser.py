from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioSyntaxAnalyzer.Parser import AbstractSyntaxParser
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNode import STDRSLSyntaxNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import STDRSLSyntaxTree
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSyntaxTokens
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLStrLiteralNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLNumberLiteralNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLBodyNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLFuncDefNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLFuncDefArgListNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLFuncDefArgNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLFuncCallNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLFuncCallArgListNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLFuncCallArgNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLExprNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLAssigmentNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLBodyLineNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLLoopNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLLoopHeaderNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLScenarioNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLLineNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLObjectNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLReturnNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.ExtendedSyntaxNode import STDRSLReturnArgNode
from RRPA.Modules.Core.General.DataStructures.WorkResult import STDWorkResult
from RRPA.Modules.Core.Logger.Logger import Logger


MODULE_PREFIX = "[Syntax Analyzer]"


class STDRSLSyntaxParser(AbstractSyntaxParser):

    def __init__(self, tokens=None, logger=Logger):
        self._logger = logger
        self._ast = None
        self._token_value = None
        self._token_type = None
        self._tokens = None
        self._cur_token_pos = None
        self._errors = []
        self.set_tokens(tokens)

    def set_tokens(self, tokens):
        self._tokens = tokens
        self._cur_token_pos = 0
        self._token_type = None
        self._token_value = None
        self._ast = None

    def _next_token(self):
        if self._cur_token_pos < len(self._tokens):
            self._token_type = self._tokens[self._cur_token_pos].get_token_type()
            self._token_value = self._tokens[self._cur_token_pos].get_token_value()
            self._cur_token_pos += 1

    def _prev_token(self):
        if self._cur_token_pos > 0:
            self._cur_token_pos -= 1
            self._token_type = self._tokens[self._cur_token_pos - 1].get_token_type()
            self._token_value = self._tokens[self._cur_token_pos - 1].get_token_value()

    def generate_ast(self):
        self._errors.clear()
        ast = self._generate_ast()
        self._ast = STDRSLSyntaxTree(ast)
        work_res = STDWorkResult()
        work_res.push(self._ast)
        work_res.push_errors(self._errors)
        return work_res

    def _generate_ast(self):
        header_node = STDRSLScenarioNode(None)
        if len(self._tokens) > 0:
            header_node.set_left_node(self._create_line_node())
            cur_node = header_node.get_left_node()
            while self._cur_token_pos < len(self._tokens):
                next_node = self._create_line_node()
                next_node.set_parent(cur_node)
                cur_node.set_right_node(next_node)
                cur_node = cur_node.get_right_node()
        return header_node

    def _error(self, error_data):
        self._logger.error(MODULE_PREFIX, error_data)
        self._errors.append(error_data)

    def _create_error_node(self, parent_node, value):
        node = STDRSLSyntaxNode(STDSyntaxTokens.UNKNOWN, value)
        node.set_parent(parent_node)
        return node

    def _create_str_literal_node(self, parent_node, value):
        node = STDRSLStrLiteralNode(value)
        node.set_parent(parent_node)
        return node

    def _create_number_literal_node(self, parent_node, value):
        node = STDRSLNumberLiteralNode(value)
        node.set_parent(parent_node)
        return node

    def _create_object_node(self, parent_node, value):
        node = STDRSLObjectNode(value)
        node.set_parent(parent_node)
        return node

    def _create_line_node(self):
        self._next_token()
        line_node = STDRSLLineNode(None)
        if self._token_type == STDSyntaxTokens.SPECIAL_INSTRUCTION:
            node = self._create_special_instruction_node(line_node, self._token_value)
        elif self._token_type == STDSyntaxTokens.FUNC_DEF:
            node = self._create_func_def_node(line_node)
        elif self._token_type == STDSyntaxTokens.OBJECT:
            node = self._create_expr_node(line_node, self._token_value)
        else:
            self._error("Ожидалось {SPEC_INST, FUNC_DEF, EXPR}, а пришло: " + self._token_value)
            node = self._create_error_node(line_node, self._token_value)
        line_node.set_left_node(node)
        return line_node

    def _create_expr_node(self, parent_node, expr_object):
        expr_node = STDRSLExprNode(None)
        expr_node.set_parent(parent_node)
        expr = self._specify_and_create_object_node(expr_node, expr_object)
        expr_node.set_left_node(expr)
        self._next_token()
        if self._token_type == STDSyntaxTokens.ENDLINE:
            return expr_node
        else:
            self._error("Ожидалось ;, а пришло: " + self._token_value)
            return self._create_error_node(expr_node, expr_object)

    def _specify_and_create_object_node(self, parent_node, object_name):
        self._next_token()
        if self._token_type == STDSyntaxTokens.SUBEXPR_START:
            return self._create_func_call_node(parent_node, object_name)
        elif self._token_type == STDSyntaxTokens.ASSIGMENT_OPERATION:
            return self._create_assigment_node(parent_node, object_name)
        else:
            self._prev_token()
            return self._create_object_node(parent_node, object_name)

    def _create_func_call_node(self, parent_node, func_name):
        func_call_node = STDRSLFuncCallNode(func_name)
        func_call_node.set_parent(parent_node)
        self._next_token()
        if self._token_type != STDSyntaxTokens.SUBEXPR_END:
            func_call_arg_list_node = self._create_func_call_arg_list_node(func_call_node)
            func_call_node.set_left_node(func_call_arg_list_node)
        return func_call_node

    def _create_func_call_arg_list_node(self, parent_node):
        func_call_arg_list_node = STDRSLFuncCallArgListNode(None)
        func_call_arg_list_node.set_parent(parent_node)
        left = self._specify_and_create_func_call_arg_node(func_call_arg_list_node)
        func_call_arg_list_node.set_left_node(left)
        if self._token_type == STDSyntaxTokens.ARG_DELIMITER:
            self._next_token()
            right = self._create_func_call_arg_list_node(func_call_arg_list_node)
            func_call_arg_list_node.set_right_node(right)
        return func_call_arg_list_node

    def _specify_and_create_func_call_arg_node(self, parent_node):
        func_call_arg_node = STDRSLFuncCallArgNode(None)
        func_call_arg_node.set_parent(parent_node)
        node = self._specify_and_create_standart_call_arg_node(func_call_arg_node)
        func_call_arg_node.set_left_node(node)
        return func_call_arg_node

    def _specify_and_create_standart_call_arg_node(self, parent_node):
        if self._token_type == STDSyntaxTokens.OBJECT:
            node = self._specify_and_create_standart_call_arg_object_node(parent_node, self._token_value)
        elif self._token_type == STDSyntaxTokens.STR_LITERAL:
            node = self._create_str_literal_node(parent_node, self._token_value)
            self._next_token()
        elif self._token_type == STDSyntaxTokens.NUMBER_LITERAL:
            node = self._create_number_literal_node(parent_node, self._token_value)
            self._next_token()
        else:
            self._error("Ожидалось имя, строка или число, а пришло: " + self._token_value)
            node = self._create_error_node(parent_node, self._token_value)
        return node

    def _specify_and_create_standart_call_arg_object_node(self, parent_node, object_name):
        self._next_token()
        if self._token_type == STDSyntaxTokens.SUBEXPR_START:
            node = self._create_func_call_node(parent_node, object_name)
            self._next_token()
        else:
            node = self._create_object_node(parent_node, object_name)
        return node

    def _create_assigment_node(self, parent_node, lvalue):
        assigment_node = STDRSLAssigmentNode(self._token_value)
        assigment_node.set_parent(parent_node)
        lvalue_node = self._create_object_node(assigment_node, lvalue)
        assigment_node.set_right_node(lvalue_node)
        rvalue = self._specify_and_create_assigment_rvalue_node(assigment_node)
        assigment_node.set_left_node(rvalue)
        return assigment_node

    def _specify_and_create_assigment_rvalue_node(self, parent_node):
        self._next_token()
        if self._token_type == STDSyntaxTokens.STR_LITERAL:
            node = self._create_str_literal_node(parent_node, self._token_value)
        elif self._token_type == STDSyntaxTokens.NUMBER_LITERAL:
            node = self._create_number_literal_node(parent_node, self._token_value)
        elif self._token_type == STDSyntaxTokens.OBJECT:
            node = self._specify_and_create_object_node(parent_node, self._token_value)
        else:
            self._error("Ожидалась строка, число или имя, а пришло: " + self._token_value)
            node = self._create_error_node(parent_node, self._token_value)
        return node

    def _create_special_instruction_node(self, parent_node, spec_inst):
        if spec_inst == "loop":
            return self._create_loop_node(parent_node)
        else:
            self._error("Ожидалось SPEC_INST, а пришло: " + spec_inst)
            return self._create_error_node(parent_node, spec_inst)

    def _create_body_special_instruction_node(self, parent_node, spec_inst):
        if spec_inst == "loop":
            return self._create_loop_node(parent_node)
        elif spec_inst == "return":
            return self._create_return_node(parent_node)
        else:
            self._error("Ожидалось SPEC_INST, а пришло: " + spec_inst)
            return self._create_error_node(parent_node, spec_inst)

    def _create_return_node(self, parent_node):
        return_node = STDRSLReturnNode("return")
        return_node.set_parent(parent_node)
        self._next_token()
        return_arg_node = self._create_return_arg_node(return_node)
        return_node.set_left_node(return_arg_node)
        return return_node

    def _create_return_arg_node(self, parent_node):
        return_arg_node = STDRSLReturnArgNode(None)
        return_arg_node.set_parent(parent_node)
        if self._token_type != STDSyntaxTokens.ENDLINE:
            node = self._specify_and_create_standart_call_arg_node(return_arg_node)
            return_arg_node.set_left_node(node)
        if self._token_type != STDSyntaxTokens.ENDLINE:
            self._error("Ожидалась ;, а пришло: " + self._token_value)
            node = self._create_error_node(parent_node, self._token_value)
            return node
        return return_arg_node

    def _create_loop_node(self, parent_node):
        loop_node = STDRSLLoopNode("loop")
        loop_node.set_parent(parent_node)
        self._next_token()
        if self._token_type == STDSyntaxTokens.SUBEXPR_START:
            loop_header_node = self._create_loop_header_node(loop_node)
            loop_node.set_left_node(loop_header_node)
            loop_body_node = self._create_loop_body_node(loop_node)
            loop_node.set_right_node(loop_body_node)
            return loop_node
        else:
            self._error("Ожидалось (, а пришло: " + self._token_value)
            return self._create_error_node(loop_node, "loop")

    def _create_loop_header_node(self, parent_node):
        self._next_token()
        loop_arg_node = STDRSLLoopHeaderNode(None)
        loop_arg_node.set_parent(parent_node)
        if self._token_type == STDSyntaxTokens.OBJECT:
            node = self._specify_and_create_loop_header_object_node(loop_arg_node, self._token_value)
        elif self._token_type == STDSyntaxTokens.NUMBER_LITERAL:
            node = self._create_number_literal_node(loop_arg_node, self._token_value)
            self._next_token()
        else:
            self._error("Ожидалось имя или число, а пришло: " + self._token_value)
            node = self._create_error_node(loop_arg_node, self._token_value)
            self._next_token()
        loop_arg_node.set_left_node(node)
        return loop_arg_node

    def _specify_and_create_loop_header_object_node(self, parent_node, object_name):
        self._next_token()
        if self._token_type == STDSyntaxTokens.SUBEXPR_START:
            node = self._create_func_call_node(parent_node, object_name)
            self._next_token()
        elif self._token_type == STDSyntaxTokens.ASSIGMENT_OPERATION:
            node = self._create_error_node(parent_node, object_name)
            self._error("Ожидалось ( или имя, а пришло: =")
        else:
            node = self._create_object_node(parent_node, object_name)
        return node

    def _create_loop_body_node(self, parent_node):
        loop_body_node = self._create_body_node(parent_node)
        return loop_body_node

    def _create_body_node(self, parent_node):
        self._next_token()
        body_node = STDRSLBodyNode(None)
        body_node.set_parent(parent_node)
        if self._token_type == STDSyntaxTokens.BODY_START:
            node = self._create_body_lines_node(body_node)
        else:
            node = self._create_error_node(body_node, self._token_value)
            self._error("Ожидалось выражение, а пришло: " + self._token_value)
        body_node.set_left_node(node)
        return body_node

    def _create_body_lines_node(self, parent_node):
        self._next_token()
        head_body_line_node = STDRSLBodyLineNode(None)
        head_body_line_node.set_parent(parent_node)
        body_line_node = head_body_line_node
        while self._token_type != STDSyntaxTokens.BODY_END:
            left_node = self._create_body_line_node(parent_node)
            right_node = STDRSLBodyLineNode(None)
            right_node.set_parent(body_line_node)
            body_line_node.set_left_node(left_node)
            body_line_node.set_right_node(right_node)
            body_line_node = body_line_node.get_right_node()
            self._next_token()
        return head_body_line_node

    def _create_body_line_node(self, parent_node):
        if self._token_type == STDSyntaxTokens.OBJECT:
            node = self._create_expr_node(parent_node, self._token_value)
        elif self._token_type == STDSyntaxTokens.SPECIAL_INSTRUCTION:
            node = self._create_body_special_instruction_node(parent_node, self._token_value)
        else:
            node = self._create_error_node(parent_node, self._token_value)
            self._error("Ожидалось тело инструкции, а пришло: " + self._token_value)
        return node

    def _create_func_def_node(self, parent_node):
        self._next_token()
        func_def_node = STDRSLFuncDefNode(self._token_value)
        func_def_node.set_parent(parent_node)
        func_def_header_node = self._create_func_def_header_node(func_def_node)
        func_def_body_node = self._create_func_def_body_node(func_def_node)
        func_def_node.set_left_node(func_def_header_node)
        func_def_node.set_right_node(func_def_body_node)
        return func_def_node

    def _create_func_def_header_node(self, parent_node):
        self._next_token()
        if self._token_type == STDSyntaxTokens.SUBEXPR_START:
            self._next_token()
            if self._token_type != STDSyntaxTokens.SUBEXPR_END:
                func_def_arg_list_node = self._create_func_def_arg_list_node(parent_node)
                return func_def_arg_list_node
            else:
                return None
        else:
            self._error("Ожидалось (, а пришло: " + self._token_value)
            return self._create_error_node(parent_node, self._token_value)

    def _create_func_def_arg_list_node(self, parent_node):
        func_def_arg_list_node = STDRSLFuncDefArgListNode(None)
        func_def_arg_list_node.set_parent(parent_node)
        left_node = self._create_func_def_arg_node(func_def_arg_list_node)
        func_def_arg_list_node.set_left_node(left_node)
        if self._token_type == STDSyntaxTokens.ARG_DELIMITER:
            self._next_token()
            right_node = self._create_func_def_arg_list_node(func_def_arg_list_node)
            func_def_arg_list_node.set_right_node(right_node)
        return func_def_arg_list_node

    def _create_func_def_arg_node(self, parent_node):
        func_def_arg_node = STDRSLFuncDefArgNode(None)
        func_def_arg_node.set_parent(parent_node)
        if self._token_type == STDSyntaxTokens.OBJECT:
            node = self._create_object_node(func_def_arg_node, self._token_value)
        else:
            self._error("Ожидалось имя, а пришло: " + self._token_value)
            node = self._create_error_node(func_def_arg_node, self._token_value)
        self._next_token()
        func_def_arg_node.set_left_node(node)
        return func_def_arg_node

    def _create_func_def_body_node(self, parent_node):
        func_def_body = self._create_body_node(parent_node)
        return func_def_body
