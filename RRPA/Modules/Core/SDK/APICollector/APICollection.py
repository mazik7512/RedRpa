from RRPA.Modules.Core.Abstract.SDK.APICollector.APICollection import AbstractAPICollection


class STDAPICollection(AbstractAPICollection):

    def __init__(self, api_file, api):
        self._api_data = api
        self._api_file = api_file
        self._api_methods = []

    def get_methods(self):
        return self._api_methods

    def add_method(self, method):
        self._api_methods.append(method)

    def get_api_name(self):
        return self._api_data[0]

    def get_api_filename(self):
        return self._api_file

    def get_class_instance(self):
        return self._api_data[1]

