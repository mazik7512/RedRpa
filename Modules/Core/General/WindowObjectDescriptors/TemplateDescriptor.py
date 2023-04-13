class TemplateDescriptor:
    def __init__(self, _points):
        self.points = _points

    def get_points(self):
        return self.points[0], self.points[1], self.points[2], self.points[3]

    def __str__(self):
        return "{points=" + str(self.points) + "}"
