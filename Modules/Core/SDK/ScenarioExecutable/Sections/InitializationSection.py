from Modules.Core.SDK.ScenarioExecutable.Sections.Section import STDSection


class STDInitSection(STDSection):

    def __init__(self):
        super().__init__()

    def deserialize(self):
        result = "@init_section:{"
        for key, data in self._table_data:
            result.join(key).join(":{").join(data).join("}").join(";")
        result.join("}")
        return result
