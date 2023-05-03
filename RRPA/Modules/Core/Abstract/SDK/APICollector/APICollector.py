from abc import ABC, abstractmethod


class AbstractAPICollector(ABC):

    @abstractmethod
    def collect_all_api_methods(self):
        pass

    @abstractmethod
    def get_all_api_methods(self):
        pass

    @abstractmethod
    def get_api_methods(self, api_name):
        pass

    @abstractmethod
    def get_api_names(self):
        pass

    @abstractmethod
    def get_api_import_path(self, api_name):
        pass

    @abstractmethod
    def get_api_name_by_func_name(self, func_name):
        pass

    @abstractmethod
    def get_func_params_by_func_name(self, func_name):
        pass
