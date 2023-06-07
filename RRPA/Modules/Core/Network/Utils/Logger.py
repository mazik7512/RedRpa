from RRPA.Modules.Core.Logger.OutputWrapper import Output
from RRPA.Modules.Core.Logger.Logger import Logger


class STDNetworkLogger(Logger):

    def __init__(self, filepath):
        self._log_file = Output(filepath, False, True)
        self._outputs_streams = [None, self._log_file]
        self._global_prefix = "[Core] [Network]"

    def info(self, *data):
        Logger.info(self._global_prefix, *data, output_params=self._outputs_streams)
