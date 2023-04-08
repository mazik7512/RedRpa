from abc import ABC, abstractmethod
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNodeDescriptor import AbstractSyntaxNodeDescriptor


class AbstractSyntaxNode(ABC):

    def __init__(self, node_descriptor: AbstractSyntaxNodeDescriptor, parent=None, left_node=None, right_node=None):
        self._parent = parent
        self._node = node_descriptor
        self._left_node = left_node
        self._right_node = right_node

    def set_type(self, _type):
        self._node.set_type(_type)

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def set_left_node(self, node):
        self._left_node = node

    def set_right_node(self, node):
        self._right_node = node

    def get_left_node(self):
        return self._left_node

    def get_right_node(self):
        return self._right_node

    def get_type(self):
        return self._node.get_type()

    def get_data(self):
        return self._node.get_data()

    def set_data(self, data):
        self._node.set_data(data)

    @abstractmethod
    def deserialize(self):
        pass
