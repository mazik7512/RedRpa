from Modules.Core.Abstract.SDK.ScenarioExecutable.Executable import AbstractExecutable
from Modules.Core.Abstract.SDK.ScenarioExecutable.SectionsContainer import AbstractSectionContainer


class STDRedExecutable(AbstractExecutable):

    def __init__(self, sections: AbstractSectionContainer, syntax_tree):
        self._sections = sections.generate()
        self._syntax_tree = syntax_tree

    def serialization(self):
        pass

    def deserialization(self) -> bytes:
        return self._sections.deserialize()
