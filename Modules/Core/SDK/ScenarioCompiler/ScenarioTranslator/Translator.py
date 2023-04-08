from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioTranslator.Translator import AbstractTranslator
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.General.DataStructures.Stack import STDStack


def translate_unit(syntax_node, result, current_condition):
    pass


class STDRSLTranslator(AbstractTranslator):
    def __init__(self, syntax_tree: AbstractSyntaxTree):
        self._tree = syntax_tree

    def translate(self):
        result = []
        current_condition = STDStack()
        self._tree.traverse("inorder", translate_unit, result, current_condition)
        return result
