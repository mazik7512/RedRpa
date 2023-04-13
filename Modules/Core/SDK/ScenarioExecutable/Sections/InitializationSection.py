from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDInitSection(STDSection):

    def __init__(self):
        super().__init__()

    def serialize(self, data):
        self._table_data = data

    def deserialize(self):
        return self._table_data

    def get_section_data(self):
        result = ""
        for init_type in self._table_data:
            for init_instance in self._table_data[init_type]:
                result += self._table_data[init_type][init_instance]['api_init_code'] + '\n'
        result += "\n\n"
        return result
