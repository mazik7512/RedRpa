import unittest
from RRPA.Modules.CVObjectScanning.ObjectScanner import STDCVObjectScanner
from RRPA.Modules.CVObjectScanning.TemplateMatcher import STDCVTemplateMatcher
from RRPA.Modules.CVObjectScanning.ObjectDetector import STDCVObjectDetector
from RRPA.AppData.Configs.ObjectDetectionConfig import MODEL_PATH


class ObjectFinderTest(unittest.TestCase):

    def test_main(self):
        od = STDCVObjectDetector("..\\..\\" + MODEL_PATH)
        tm = STDCVTemplateMatcher()
        of = STDCVObjectScanner(tm, od)
        objects = of.find_objects("..\\..\\Tests\\TestImages\\test-3.png")
        print(*objects)


if __name__ == "__main__":
    unittest.main(verbosity=2)
