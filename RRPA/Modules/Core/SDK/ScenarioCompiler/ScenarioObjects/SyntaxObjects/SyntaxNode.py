from RRPA.Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNode import AbstractSyntaxNode
from RRPA.Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNodeDescriptor import STDRSLSyntaxNodeDescriptor


class STDRSLSyntaxNode(AbstractSyntaxNode):

    def __init__(self, node_type, node_data):
        node_desc = STDRSLSyntaxNodeDescriptor(node_type, node_data)
        super().__init__(node_desc)

    def deserialize(self):
        return self.get_data()

    def __str__(self):
        _type = self.get_type()
        _data = self.get_data()
        res = "[Node: type=" + str(_type)
        if _data:
            res += ", data=" + str(_data)
        left = self.get_left_node()
        if left:
            res += ", left=" + str(left)
        right = self.get_right_node()
        if right:
            res += ", right=" + str(right)
        res += "]"
        return res
