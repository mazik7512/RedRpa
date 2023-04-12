from Modules.Core.Abstract.SDK.ScenarioExecutable.ExecutableGenerator import AbstractExecutableGenerator
from Modules.Core.SDK.ScenarioExecutable.SectionsContainer import STDSectionContainer
from Modules.Core.SDK.ScenarioExecutable.Sections.InfoSection import STDInfoSection
from Modules.Core.SDK.ScenarioExecutable.Sections.ImportsSection import STDImportsSection
from Modules.Core.SDK.ScenarioExecutable.Sections.InitializationSection import STDInitSection
from Modules.Core.SDK.ScenarioExecutable.Sections.ExecutableSection import STDExecSection


class STDREXGenerator(AbstractExecutableGenerator):

    def __init__(self):
        self._sections = STDSectionContainer()

    def _add_import_section(self, import_data):
        import_section = STDImportsSection()
        import_section.add("api", import_data)
        self._sections.add_section("import", import_section)

    def _add_init_section(self, init_data):
        init_section = STDInitSection()
        init_section.add("api_init", init_data)
        self._sections.add_section("init", init_section)

    def _add_info_section(self):
        info_section = STDInfoSection()
        self._sections.add_section("info", info_section)

    def _add_user_code_section(self, user_code):
        user_code_section = STDExecSection()
        user_code_section.add("user_code", user_code)
        self._sections.add_section("user_code", user_code_section)

    def add_section(self, section_type: str, section_data):
        func_name = "_add_" + section_type + "_section"
        section_adder = getattr(self, func_name)
        section_adder(section_data)

    def generate_executable_sections(self):
        self._add_info_section()
        return self._sections
