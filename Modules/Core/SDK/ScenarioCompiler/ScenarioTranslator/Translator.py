from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioTranslator.Translator import AbstractTranslator
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.General.DataStructures.WorkResult import STDWorkResult
from Modules.Core.Logger.Logger import Logger


class STDRSLTranslator(AbstractTranslator):
    def __init__(self, syntax_tree=None, logger=Logger):
        self._logger = logger
        self._tree = syntax_tree
        self._errors = []

    def translate(self):
        work_res = STDWorkResult()
        result = self._tree.get_head().deserialize()
        work_res.push(result)
        work_res.push_errors(self._errors)
        return work_res

    def set_data(self, data):
        self._tree = data
        self._errors = []
