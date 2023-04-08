from Modules.Core.Abstract.SDK.ScenarioExecutable.SectionsContainer import AbstractSectionContainer
from Modules.Core.SDK.ScenarioExecutable.Sections.ExecutableSection import STDExecSection
from Modules.Core.SDK.ScenarioExecutable.Sections.ImportsSection import STDImportsSection
from Modules.Core.SDK.ScenarioExecutable.Sections.InfoSection import STDInfoSection


class STDSectionContainer(AbstractSectionContainer):

    def __init__(self):
        self._sections = {}

    def get_section(self, section):
        return self._sections[section]

    def add_section(self, section, section_data):
        self._sections[section] = section_data

    def add_section_data(self, section, data):
        self._sections[section] = data

    def deserialize(self):
        result = "sections:{"
        for key, section in self._sections:
            result.join(section.deserialize()).join("\n")
        result.join("}")
        return result

    def generate(self):
        self.add_section('info', STDInfoSection())
        self.add_section('import', STDImportsSection())
        self.add_section('user_code', STDExecSection())
