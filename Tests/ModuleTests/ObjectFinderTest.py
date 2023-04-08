import unittest
from Modules.ObjectDetection.ObjectFinder import ObjFinder
from Modules.ObjectDetection.OpenCVTemplateMatcher import OpenCVTemplateMatcher
from Modules.ObjectDetection.TFObjectDetector import TFObjectDetector
from AppData.Configs.ObjectDetectionConfig import MODEL_PATH


class ObjectFinderTest(unittest.TestCase):

    def test_main(self):
        od = TFObjectDetector("..\\..\\" + MODEL_PATH)
        tm = OpenCVTemplateMatcher()
        of = ObjFinder(tm, od)
        objects = of.find_objects("..\\..\\Tests\\TestImages\\test-3.png")
        print(*objects)


if __name__ == "__main__":
    unittest.main(verbosity=2)
