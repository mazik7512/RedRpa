from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNodeDescriptor import AbstractSyntaxNodeDescriptor


class STDRSLSyntaxNodeDescriptor(AbstractSyntaxNodeDescriptor):

    def __init__(self, node_type, node_data):
        self._type = node_type
        self._data = node_data

    def set_type(self, _type):
        self._type = _type

    def get_type(self):
        return self._type

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
