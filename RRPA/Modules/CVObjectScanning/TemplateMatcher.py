import cv2
from RRPA.Modules.Core.Abstract.ObjectScanning.TemplateMatcher import AbstractTemplateMatcher
from RRPA.Modules.Core.General.WindowObjectsDescriptors.TemplateDescriptor import STDTemplateDescriptor


class STDCVTemplateMatcher(AbstractTemplateMatcher):

    def find_templates(self, image) -> list:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)  # Blur to reduce noise
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        ret, thresh1 = cv2.threshold(gray, 0, 100, cv2.THRESH_OTSU |
                                     cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))  # 2, 2
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=4)
        #dst = cv2.erode(dilation, rect_kernel, iterations=1)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
        templates = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            temp = [x, x + w, y, y + h]
            obj = STDTemplateDescriptor(temp)
            templates.append(obj)
        return templates
