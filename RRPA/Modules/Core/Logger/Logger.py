from RRPA.Modules.Core.Abstract.Logger.Logger import AbstractLogger
from RRPA.Modules.Core.Logger.LogColors import CmdColorizer
from datetime import datetime
from RRPA.Modules.Core.Logger.OutputWrapper import Output
import threading


class Logger(AbstractLogger):
    Colorizer = CmdColorizer
    __ERROR = "[ОШИБКА]"
    __WARNING = "[ПРЕДУПРЕЖДЕНИЕ]"
    __SUCCESS = "[УСПЕШНО]"
    __INFO = "[ИНФОРМАЦИЯ]"
    __OUTPUTS = [None]
    __locker = threading.Lock()

    @staticmethod
    def add_output_file(filepath: str, colorization=False, timing=True):
        ow = Output(filepath, colorization, timing)
        Logger.__OUTPUTS.append(ow)

    @staticmethod
    def __print(*data, color_start, time, event_type, color_end=Colorizer.DEFAULT, output_params=None):
        Logger.__locker.acquire()
        output_streams = Logger.__OUTPUTS
        if output_params:
            output_streams = output_params
        for output in output_streams:
            start_color = color_start
            cur_time = time
            end_color = color_end
            log_file = None
            if output is not None:
                start_color = color_start if output.colorization else ""
                cur_time = time if output.timings else ""
                end_color = color_end if output.colorization else ""
                log_file = open(output.path, "a")
            print(start_color, cur_time, event_type, *data, end_color, file=log_file)
            if output is not None:
                log_file.close()
        Logger.__locker.release()

    @staticmethod
    def error(*data, output_params=None) -> None:
        cur_time = datetime.now()
        Logger.__print(*data, color_start=Logger.Colorizer.FAIL, time=cur_time,
                       event_type=Logger.__ERROR, output_params=output_params)

    @staticmethod
    def success(*data, output_params=None) -> None:
        cur_time = datetime.now()
        Logger.__print(*data, color_start=Logger.Colorizer.OKGREEN, time=cur_time,
                       event_type=Logger.__SUCCESS, output_params=output_params)

    @staticmethod
    def warning(*data, output_params=None) -> None:
        cur_time = datetime.now()
        Logger.__print(*data, color_start=Logger.Colorizer.WARNING, time=cur_time,
                       event_type=Logger.__WARNING, output_params=output_params)

    @staticmethod
    def info(*data, output_params=None) -> None:
        cur_time = datetime.now()
        Logger.__print(*data, color_start=Logger.Colorizer.HEADER, time=cur_time,
                       event_type=Logger.__INFO, output_params=output_params)
