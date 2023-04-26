import unittest
from RRPA.Modules.CVObjectScanning.TemplateMatcher import STDCVTemplateMatcher
import os
from RRPA.AppData.Configs.TestConfig import TEST_IMAGES_PATH
import cv2


class TestTemplateMatching(unittest.TestCase):

    def test_main(self):
        template_test = STDCVTemplateMatcher()
        test_images = [f for f in os.listdir(TEST_IMAGES_PATH) if os.path.isfile(os.path.join(TEST_IMAGES_PATH, f))]
        for image in test_images:
            _image = cv2.imread(TEST_IMAGES_PATH + image, cv2.IMREAD_COLOR)
            templates = template_test.find_templates(_image)
            for template in templates:
                cv2.imshow(image, template)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


if __name__ == "__main__":
    unittest.main(verbosity=3)
