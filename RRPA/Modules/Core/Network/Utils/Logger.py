from RRPA.Modules.Core.Logger.OutputWrapper import Output
from RRPA.Modules.Core.Logger.Logger import Logger


class STDNetworkLogger:

    def __init__(self, filepath):
        self._log_file = Output(filepath, False, True)
        self._outputs_streams = [None, self._log_file]
        self._global_prefix = "[Core] [Network]"

    def debug(self, prefix, *data):
        Logger.info(self._global_prefix, prefix, *data, output_params=self._outputs_streams)
