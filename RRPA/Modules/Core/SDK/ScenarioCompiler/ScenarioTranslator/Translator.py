from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioTranslator.Translator import AbstractTranslator
from RRPA.Modules.Core.General.DataStructures.WorkResult import STDWorkResult
from RRPA.Modules.Core.Logger.Logger import Logger
from RRPA.Modules.Core.Exceptions.Exceptions import STDTranslationException


class STDRSLTranslator(AbstractTranslator):
    def __init__(self, syntax_tree=None, logger=Logger):
        self._logger = logger
        self._tree = syntax_tree
        self._errors = []

    def translate(self):
        self._errors.clear()
        work_res = STDWorkResult()
        try:
            result = self._tree.get_head().deserialize()
            work_res.push(result)
        except STDTranslationException as e:
            self._errors.append(e.get_exception_data())
        finally:
            work_res.push_errors(self._errors)
            return work_res

    def set_data(self, data):
        self._tree = data
        self._errors = []
