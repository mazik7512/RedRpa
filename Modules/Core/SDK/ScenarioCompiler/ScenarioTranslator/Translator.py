from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioTranslator.Translator import AbstractTranslator
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.General.DataStructures.Stack import STDStack


def get_translation_units(syntax_node, result, current_state):
    data = syntax_node.get_data()
    if data:
        result.append(data)


class STDRSLTranslator(AbstractTranslator):
    def __init__(self, syntax_tree: AbstractSyntaxTree):
        self._tree = syntax_tree

    def translate(self):
        result = self._tree.get_head().deserialize()
        print("\tТРАНСЛЯЦИЯ:")
        print(result)
        #result = []
        #current_condition = STDStack()
        #self._tree.traverse("inorder", get_translation_units, result, current_condition)
        #print(result)
        #return result
