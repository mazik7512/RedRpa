from RRPA.Modules.Core.Abstract.SDK.ScenarioExecutable.Executable import AbstractExecutable
from RRPA.Modules.Core.Abstract.SDK.ScenarioExecutable.SectionsContainer import AbstractSectionContainer
from RRPA.Modules.Core.SDK.ScenarioExecutable.SectionsContainer import STDSectionContainer


class STDRedExecutable(AbstractExecutable):

    def __init__(self, sections: AbstractSectionContainer = STDSectionContainer()):
        self._sections = sections

    def serialize(self, data: str):
        self._sections.serialize(data)

    def deserialize(self):
        return self._sections.deserialize()

    def get_sections(self):
        return self._sections

    def __str__(self):
        return self.deserialize()
