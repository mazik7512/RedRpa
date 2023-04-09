from Modules.Core.Abstract.SDK.ScenarioCompiler.SyntaxAnalyzer.Parser import AbstractSyntaxParser
from Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNode import STDRSLSyntaxNode
from Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import STDRSLSyntaxTree
from Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDSyntaxTokens


class STDRSLSyntaxParser(AbstractSyntaxParser):

    def __init__(self, tokens):
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
        ast = self._generate_ast()
        self._ast = STDRSLSyntaxTree(ast)
        return self._ast

    def _generate_ast(self):
        header_node = STDRSLSyntaxNode(STDSyntaxTokens.SCENARIO, None)
        header_node.set_left_node(self._create_line_node())
        cur_node = header_node
        while self._cur_token_pos < len(self._tokens):
            next_node = self._create_line_node()
            next_node.set_parent(cur_node)
            cur_node.set_right_node(next_node)
            cur_node = cur_node.get_right_node()
        return header_node

    def _error(self, error_data):
        print(error_data)

    def _create_error_node(self, parent_node, value):
        node = STDRSLSyntaxNode(STDSyntaxTokens.UNKNOWN, value)
        node.set_parent(parent_node)
        return node

    def _create_str_literal_node(self, parent_node, value):
        node = STDRSLSyntaxNode(STDSyntaxTokens.STR_LITERAL, value)
        node.set_parent(parent_node)
        return node

    def _create_number_literal_node(self, parent_node, value):
        node = STDRSLSyntaxNode(STDSyntaxTokens.NUMBER_LITERAL, value)
        node.set_parent(parent_node)
        return node

    def _create_object_node(self, parent_node, value):
        node = STDRSLSyntaxNode(STDSyntaxTokens.OBJECT, value)
        node.set_parent(parent_node)
        return node

    def _create_line_node(self):
        self._next_token()
        line_node = STDRSLSyntaxNode(STDSyntaxTokens.LINE, None)
        if self._token_type == STDSyntaxTokens.SPECIAL_INSTRUCTION:
            node = self._create_special_instruction_node(line_node, self._token_value)
        elif self._token_type == STDSyntaxTokens.FUNC_DEF:
            node = self._create_func_def_node(line_node)
        elif self._token_type == STDSyntaxTokens.OBJECT:
            node = self._create_expr_node(line_node, self._token_value)
        else:
            self._error("Line Node")
            node = self._create_error_node(line_node, self._token_value)
        line_node.set_left_node(node)
        return line_node

    def _create_expr_node(self, parent_node, expr_object):
        expr_node = self._specify_and_create_object_node(parent_node, expr_object)
        self._next_token()
        if self._token_type == STDSyntaxTokens.ENDLINE:
            return expr_node
        else:
            self._error("Expr")
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
        func_call_node = STDRSLSyntaxNode(STDSyntaxTokens.FUNC_CALL, func_name)
        func_call_node.set_parent(parent_node)
        self._next_token()
        if self._token_type != STDSyntaxTokens.SUBEXPR_END:
            func_call_arg_list_node = self._create_func_call_arg_list_node(func_call_node)
            func_call_node.set_left_node(func_call_arg_list_node)
        return func_call_node

    def _create_func_call_arg_list_node(self, parent_node):
        func_call_arg_list_node = STDRSLSyntaxNode(STDSyntaxTokens.FUNC_CALL_ARG_LIST, None)
        func_call_arg_list_node.set_parent(parent_node)
        left = self._specify_and_create_func_call_arg_node(func_call_arg_list_node)
        func_call_arg_list_node.set_left_node(left)
        if self._token_type == STDSyntaxTokens.ARG_DELIMITER:
            self._next_token()
            right = self._create_func_call_arg_list_node(func_call_arg_list_node)
            func_call_arg_list_node.set_right_node(right)
        return func_call_arg_list_node

    def _specify_and_create_func_call_arg_node(self, parent_node):
        func_call_arg = STDRSLSyntaxNode(STDSyntaxTokens.FUNC_CALL_ARG, None)
        func_call_arg.set_parent(parent_node)
        if self._token_type == STDSyntaxTokens.OBJECT:
            node = self._specify_and_create_func_call_object_arg_node(func_call_arg, self._token_value)
        elif self._token_type == STDSyntaxTokens.STR_LITERAL:
            node = self._create_str_literal_node(func_call_arg, self._token_value)
            self._next_token()
        elif self._token_type == STDSyntaxTokens.NUMBER_LITERAL:
            node = self._create_number_literal_node(func_call_arg, self._token_value)
            self._next_token()
        else:
            self._error("Func_arg")
            node = self._create_error_node(func_call_arg, self._token_value)
        func_call_arg.set_left_node(node)
        return func_call_arg

    def _specify_and_create_func_call_object_arg_node(self, parent_node, object_name):
        self._next_token()
        if self._token_type == STDSyntaxTokens.SUBEXPR_START:
            node = self._create_func_call_node(parent_node, object_name)
            self._next_token()
        else:
            node = self._create_object_node(parent_node, object_name)
        return node

    def _create_assigment_node(self, parent_node, lvalue):
        assigment_node = STDRSLSyntaxNode(STDSyntaxTokens.ASSIGMENT_OPERATION, self._token_value)
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
            self._error("assigment rvalue")
            node = self._create_error_node(parent_node, self._token_value)
        return node

    def _create_special_instruction_node(self, parent_node, spec_inst):
        if spec_inst == "loop":
            return self._create_loop_node(parent_node)
        else:
            self._error("Spec inst")
            return self._create_error_node(parent_node, spec_inst)

    def _create_loop_node(self, parent_node):
        loop_node = STDRSLSyntaxNode(STDSyntaxTokens.SPECIAL_INSTRUCTION, "loop")
        loop_node.set_parent(parent_node)
        self._next_token()
        if self._token_type == STDSyntaxTokens.SUBEXPR_START:
            loop_header_node = self._create_loop_header_node(loop_node)
            loop_node.set_left_node(loop_header_node)
            loop_body_node = self._create_loop_body_node(loop_node)
            loop_node.set_right_node(loop_body_node)
            return loop_node
        else:
            self._error("loop node")
            return self._create_error_node(loop_node, "loop")

    def _create_loop_header_node(self, parent_node):
        self._next_token()
        loop_arg_node = STDRSLSyntaxNode(STDSyntaxTokens.LOOP_ARG, None)
        loop_arg_node.set_parent(parent_node)
        if self._token_type == STDSyntaxTokens.OBJECT:
            node = self._specify_and_create_loop_header_object_node(loop_arg_node, self._token_value)
        elif self._token_type == STDSyntaxTokens.NUMBER_LITERAL:
            node = self._create_number_literal_node(loop_arg_node, self._token_value)
            self._next_token()
        else:
            self._error(self._token_value)
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
            self._error(object_name)
        else:
            node = self._create_object_node(parent_node, object_name)
        return node

    def _create_loop_body_node(self, parent_node):
        loop_body_node = self._create_body_node(parent_node)
        return loop_body_node

    def _create_body_node(self, parent_node):
        self._next_token()
        body_node = STDRSLSyntaxNode(STDSyntaxTokens.BODY, None)
        body_node.set_parent(parent_node)
        if self._token_type == STDSyntaxTokens.BODY_START:
            node = self._create_body_lines_node(body_node)
        else:
            node = self._create_error_node(body_node, self._token_value)
            self._error(self._token_value)
        body_node.set_left_node(node)
        return body_node

    def _create_body_lines_node(self, parent_node):
        self._next_token()
        head_body_line_node = STDRSLSyntaxNode(STDSyntaxTokens.BODY_LINE, None)
        head_body_line_node.set_parent(parent_node)
        body_line_node = head_body_line_node
        while self._token_type != STDSyntaxTokens.BODY_END:
            left_node = self._create_body_line_node(parent_node)
            right_node = STDRSLSyntaxNode(STDSyntaxTokens.BODY_LINE, None)
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
            node = self._create_special_instruction_node(parent_node, self._token_value)
        else:
            node = self._create_error_node(parent_node, self._token_value)
            self._error("body line")
        return node

    def _create_func_def_node(self, parent_node):
        self._next_token()
        func_def_node = STDRSLSyntaxNode(STDSyntaxTokens.FUNC_DEF, self._token_value)
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
            self._error("func def arg list")
            return self._create_error_node(parent_node, self._token_value)

    def _create_func_def_arg_list_node(self, parent_node):
        func_def_arg_list_node = STDRSLSyntaxNode(STDSyntaxTokens.FUNC_DEF_ARG_LIST, None)
        func_def_arg_list_node.set_parent(parent_node)
        left_node = self._create_func_def_arg_node(func_def_arg_list_node)
        func_def_arg_list_node.set_left_node(left_node)
        if self._token_type == STDSyntaxTokens.ARG_DELIMITER:
            self._next_token()
            right_node = self._create_func_def_arg_list_node(func_def_arg_list_node)
            func_def_arg_list_node.set_right_node(right_node)
        return func_def_arg_list_node

    def _create_func_def_arg_node(self, parent_node):
        func_def_arg_node = STDRSLSyntaxNode(STDSyntaxTokens.FUNC_DEF_ARG, None)
        func_def_arg_node.set_parent(parent_node)
        if self._token_type == STDSyntaxTokens.OBJECT:
            node = self._create_object_node(func_def_arg_node, self._token_value)
        else:
            self._error(self._token_value)
            node = self._create_error_node(func_def_arg_node, self._token_value)
        self._next_token()
        func_def_arg_node.set_left_node(node)
        return func_def_arg_node

    def _create_func_def_body_node(self, parent_node):
        func_def_body = self._create_body_node(parent_node)
        return func_def_body
