from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDImportsSection(STDSection):

    def __init__(self):
        super().__init__()

    def deserialize(self):
        result = "@import_section:{"
        for key, data in self._table_data:
            result.join(key).join("{").join(data).join("}").join(";")
        result.join("}")
        return result
