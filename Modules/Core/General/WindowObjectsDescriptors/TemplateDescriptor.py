from Modules.Core.Abstract.General.WindowObjectsDescriptors.TemplateDescriptor import AbstractTemplateDescriptor


class STDTemplateDescriptor(AbstractTemplateDescriptor):
    def __init__(self, _points):
        self._points = _points

    def get_points(self):
        return self._points[0], self._points[1], self._points[2], self._points[3]

    def __str__(self):
        return "{points=" + str(self._points) + "}"
