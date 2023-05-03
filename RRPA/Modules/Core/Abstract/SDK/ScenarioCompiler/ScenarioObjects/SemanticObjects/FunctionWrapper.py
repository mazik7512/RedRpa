from abc import ABC, abstractmethod


class AbstractFunctionWrapper(ABC):

    @abstractmethod
    def get_func_name(self):
        pass

    @abstractmethod
    def get_func_args_count(self):
        pass

    @abstractmethod
    def get_func_args_types(self):
        pass

    @abstractmethod
    def get_func_arg_type(self, index):
        pass

    @abstractmethod
    def get_func_type(self):
        pass
