from RRPA.Modules.Core.Abstract.SDK.ScenarioExecutable.SectionsContainer import AbstractSectionContainer
from RRPA.Modules.Core.SDK.ScenarioExecutable.Sections.ImportSection import STDImportSection
from RRPA.Modules.Core.SDK.ScenarioExecutable.Sections.InitializationSection import STDInitSection
from RRPA.Modules.Core.SDK.ScenarioExecutable.Sections.ExecutableSection import STDExecSection
from RRPA.Modules.Core.SDK.ScenarioExecutable.Sections.InfoSection import STDInfoSection
import json


class STDSectionContainer(AbstractSectionContainer):

    def __init__(self):
        self._sections = {}

    def get_section(self, section):
        return self._sections[section]

    def get_keys(self):
        return self._sections.keys()

    def add_section(self, section, section_data):
        self._sections[section] = section_data

    def add_section_data(self, section, data):
        self._sections[section] = data

    def deserialize(self):
        _buffer = {}
        for key in self._sections:
            _buffer[key] = self._sections[key].deserialize()
        return json.dumps(_buffer)

    def serialize(self, data):
        sections = json.loads(data)
        for key in sections:
            self._sections[key] = self._serialize_section(key, sections[key])

    def _serialize_section(self, section_name, section_data):
        if section_name == "info_section":
            return self._serialize_info_section(section_data)
        elif section_name == "import_section":
            return self._serialize_import_section(section_data)
        elif section_name == "init_section":
            return self._serialize_init_section(section_data)
        elif section_name == "user_code_section":
            return self._serialize_user_code_section(section_data)

    def _serialize_info_section(self, info_data):
        info_section = STDInfoSection()
        info_section.serialize(info_data)
        return info_section

    def _serialize_import_section(self, import_data):
        import_section = STDImportSection()
        import_section.serialize(import_data)
        return import_section

    def _serialize_init_section(self, init_data):
        init_section = STDInitSection()
        init_section.serialize(init_data)
        return init_section

    def _serialize_user_code_section(self, user_code_data):
        user_code_section = STDExecSection()
        user_code_section.serialize(user_code_data)
        return user_code_section
