from RRPA.Modules.Core.Abstract.SDK.VirtualMachine.VM import AbstractVirtualMachine
from RRPA.Modules.Core.Exceptions.Exceptions import STDRVMRuntimeException, STDREXCorruptionException
from RRPA.Modules.Core.SDK.ScenarioExecutable.Executable import STDRedExecutable
from RRPA.Modules.Core.Crypto.StribogHasher import STDHasher
from RRPA.Modules.Core.Logger.Logger import Logger


class STDRedVirtualMachine(AbstractVirtualMachine):

    def __init__(self):
        self._errors = []

    def execute(self,  file: STDRedExecutable):
        self._errors.clear()
        self._analyze_and_execute(file)

    def _analyze_and_execute(self, file: STDRedExecutable):
        rex_dump = file.get_sections()
        rex_standart = rex_dump.get_section('info_section').get_data_by_name('executable_standart')
        executor_name = "_execute_" + rex_standart + "_rex"
        executor = getattr(self, executor_name)
        executor(rex_dump)

    def _error(self, error_data):
        self._errors.append(error_data)
        Logger.error(error_data)

    def _hash_check(self, rex_hash, rex):
        hasher = STDHasher()
        new_hash = hasher.hash_string(rex)
        if rex_hash == new_hash:
            return True
        else:
            return False

    def _execute_STD_rex(self, sections):
        script = ""
        rex_hash = sections.get_section('info_section').get_data_by_name('executable_hash')
        for key in sections.get_keys():
            if key != "info_section":
                script += self._dump_section(sections.get_section(key))
        check = self._hash_check(rex_hash, script)
        if check:
            self._execute(script)
        else:
            error_data = "Файл сценария поврежден"
            self._error(error_data)
            corrupted_scenario_exception = STDREXCorruptionException(self._errors)
            raise corrupted_scenario_exception

    def _execute(self, source_code):
        try:
            exec(source_code)
        except Exception as e:
            error_data = "Ошибка выполнения: " + str(e)
            self._error(error_data)
            runtime_exception = STDRVMRuntimeException(self._errors)
            raise runtime_exception

    def _dump_section(self, section):
        result = ""
        result += section.get_section_data()
        return result

