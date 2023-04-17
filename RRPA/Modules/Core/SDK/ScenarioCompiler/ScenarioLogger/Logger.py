from RRPA.Modules.Core.Logger.OutputWrapper import Output
from RRPA.Modules.Core.Logger.Logger import Logger


class STDCompilerLogger:

    def __init__(self, filepath):
        self._log_file = Output(filepath, False, True)
        self._outputs_streams = [None, self._log_file]
        self._global_prefix = "[Core] [Compiler]"

    def error(self, prefix, *data):
        Logger.error(self._global_prefix, prefix, *data, output_params=self._outputs_streams)

    def success(self, prefix, *data):
        Logger.success(self._global_prefix, prefix, *data, output_params=self._outputs_streams)
