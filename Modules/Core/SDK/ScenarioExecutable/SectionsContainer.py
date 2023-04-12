from Modules.Core.Abstract.SDK.ScenarioExecutable.SectionsContainer import AbstractSectionContainer


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
        for key in self._sections:
            result += self._sections[key].deserialize() + "\n"
        result += "}"
        return result

