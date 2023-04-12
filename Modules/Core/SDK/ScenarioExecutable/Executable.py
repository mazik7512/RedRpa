from Modules.Core.Abstract.SDK.ScenarioExecutable.Executable import AbstractExecutable
from Modules.Core.Abstract.SDK.ScenarioExecutable.SectionsContainer import AbstractSectionContainer


class STDRedExecutable(AbstractExecutable):

    def __init__(self, sections: AbstractSectionContainer):
        self._sections = sections

    def serialization(self):
        pass

    def deserialization(self) -> bytes:
        return self._sections.deserialize()

    def __str__(self):
        return self.deserialization()
