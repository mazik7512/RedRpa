from RRPA.Modules.CVObjectScanning.TemplateMatcher import STDCVTemplateMatcher
from RRPA.Modules.CVObjectScanning.ObjectDetector import STDCVObjectDetector
from RRPA.Modules.CVObjectScanning.ObjectScanner import STDCVObjectScanner
from RRPA.AppData.Configs.ObjectDetectionConfig import MODEL_PATH


class STDCVObjectScannerGenerator:

    @staticmethod
    def generate_cv_object_scanner():
        matcher = STDCVTemplateMatcher()
        detector = STDCVObjectDetector(MODEL_PATH)
        scanner = STDCVObjectScanner(matcher, detector)
        return scanner
