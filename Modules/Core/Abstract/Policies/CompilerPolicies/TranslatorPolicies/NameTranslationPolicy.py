from abc import ABC, abstractmethod


class AbstractNameTranslationPolicy(ABC):

    @staticmethod
    @abstractmethod
    def generate_loop_arg_name(*args):
        pass

    @staticmethod
    @abstractmethod
    def generate_func_call_arg_name(*args):
        pass
