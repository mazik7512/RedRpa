from Modules.Core.Abstract.SDK.VirtualMachine.VM import AbstractVirtualMachine
from Modules.Core.SDK.ScenarioExecutable.Executable import STDRedExecutable


class STDRedVirtualMachine(AbstractVirtualMachine):

    def execute(self,  file: STDRedExecutable):
        self._analyze_and_execute(file)

    def _analyze_and_execute(self, file: STDRedExecutable):
        rex_dump = file.get_sections()
        rex_standart = rex_dump.get_section('info_section').get_data_by_name('executable_standart')
        executor_name = "_execute_" + rex_standart + "_rex"
        executor = getattr(self, executor_name)
        executor(rex_dump)

    def _execute_STD_rex(self, sections):
        script = ""
        for key in sections.get_keys():
            if key != "info_section":
                script += self._dump_section(sections.get_section(key))
        self._execute(script)

    def _execute(self, source_code):
        try:
            exec(source_code)
        except:
            print("RUNTIME ERROR")

    def _dump_section(self, section):
        result = ""
        result += section.get_section_data()
        return result

