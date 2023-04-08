from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTreeIterator import AbstractSyntaxTreeIterator


class STDRSLPreOrderSyntaxTreeIterator(AbstractSyntaxTreeIterator):

    def __init__(self, syntax_tree: AbstractSyntaxTree):
        self._tree = syntax_tree

    def traverse(self, root=None, func=None, *func_args):
        if not root:
            root = self._tree.get_head()
        if func:
            func(root, *func_args)
        left = root.get_left_node()
        if left:
            self.traverse(left, func, *func_args)
        right = root.get_right_node()
        if right:
            self.traverse(right, func, *func_args)


class STDRSLInOrderSyntaxTreeIterator(AbstractSyntaxTreeIterator):

    def __init__(self, syntax_tree: AbstractSyntaxTree):
        self._tree = syntax_tree

    def traverse(self, root=None, func=None, *func_args):
        if not root:
            root = self._tree.get_head()
        left = root.get_left_node()
        if left:
            self.traverse(left, func, *func_args)
        if func:
            func(root, *func_args)
        right = root.get_right_node()
        if right:
            self.traverse(right, func, *func_args)
