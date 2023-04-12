from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioTranslator.Translator import AbstractTranslator
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.Logger.Logger import Logger


class STDRSLTranslator(AbstractTranslator):
    def __init__(self, syntax_tree=None, logger=Logger):
        self._logger = logger
        self._tree = syntax_tree

    def translate(self):
        result = self._tree.get_head().deserialize()
        return result

    def set_data(self, data):
        self._tree = data
