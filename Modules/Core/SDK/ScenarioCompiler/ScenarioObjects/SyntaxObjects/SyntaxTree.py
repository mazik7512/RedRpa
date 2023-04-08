from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNode import AbstractSyntaxNode
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTreeIterator import \
    STDRSLPreOrderSyntaxTreeIterator, STDRSLInOrderSyntaxTreeIterator


class STDRSLSyntaxTree(AbstractSyntaxTree):

    def __init__(self, header_node: AbstractSyntaxNode):
        self._header_node = header_node

    def deserialize(self):
        self._header_node.deserialize()

    def traverse(self, traverse_type: str, func, *func_args):
        if traverse_type == "preorder":
            iterator = STDRSLPreOrderSyntaxTreeIterator(self)
            iterator.traverse(self._header_node, func, *func_args)
        elif traverse_type == "inorder":
            iterator = STDRSLInOrderSyntaxTreeIterator(self)
            iterator.traverse(self._header_node, func, *func_args)

    def get_head(self):
        return self._header_node
