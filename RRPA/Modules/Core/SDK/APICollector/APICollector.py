from RRPA.Modules.Core.Abstract.SDK.APICollector.APICollector import AbstractAPICollector
from RRPA.Modules.Core.SDK.APICollector.APICollection import STDAPICollection
import inspect
import os
import importlib
from RRPA.Modules.Core.Logger.Logger import Logger
from RRPA.Modules.Core.SDK.APICollector.APIObject import STDAPIObject


class STDAPICollector(AbstractAPICollector):

    def __init__(self, path, logger=Logger):
        self._path = path
        self._api_functions = []

    def _get_api_list(self):
        api_list = os.listdir(self._path)
        return api_list

    def collect_all_api_methods(self):
        api_list = os.listdir(os.getcwd() + "\\" + self._path)
        modules = filter(lambda x: x.endswith('.py'), api_list)
        for m in modules:
            module = importlib.import_module(self._path.replace("\\", ".") + m[0:-3])
            module_classes = inspect.getmembers(module, inspect.isclass)
            class_data = filter(lambda x: not x[0].startswith('Abstract') and x[0].endswith('API'), module_classes)
            module_api = STDAPICollection(m[0:-3], *class_data)
            functions = inspect.getmembers(module_api.get_class_instance(), inspect.isfunction)
            functions = filter(lambda x: not x[0].startswith('_'), functions)
            for func in functions:
                args = inspect.signature(func[1])
                _args = []
                for arg in args.parameters.items():
                    if arg[0] != "self":
                        _args.append(str(arg[1]))
                api_function = STDAPIObject(func[0], _args)
                module_api.add_method(api_function)
            self._api_functions.append(module_api)

    def get_all_api_methods(self):
        return [func.get_object_name() for api in self._api_functions for func in api.get_methods()]

    def get_api_methods(self, api_name):
        api_methods = []
        for api in self._api_functions:
            if api_name == api.get_api_name():
                methods = api.get_methods()
                for method in methods:
                    api_methods.append(method.get_object_name())

    def get_api_names(self):
        api_names_list = [api_name.get_api_name() for api_name in self._api_functions]
        return api_names_list

    def get_api_import_path(self, api_name):
        filename = ""
        for api in self._api_functions:
            if api_name == api.get_api_name():
                filename = api.get_api_filename()
        return self._path.replace("\\", ".") + filename

    def get_api_name_by_func_name(self, func_name):
        for api in self._api_functions:
            for method in api.get_methods():
                if method.get_object_name() == func_name:
                    return api.get_api_name()

    def get_func_params_by_func_name(self, func_name):
        params = [func.get_object_data() for api in self._api_functions for func in api.get_methods() if func.get_object_name() == func_name]
        return params[0]
