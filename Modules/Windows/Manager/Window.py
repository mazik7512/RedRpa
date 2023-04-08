from Modules.Core.Abstract.OS.Manager.Window import AbstractWindow
import win32gui
import win32ui
from ctypes import windll
import PIL.Image as Image
import io


class STDWindow(AbstractWindow):

    def __init__(self, window):
        super().__init__(window)

    def get_window_title(self) -> str:
        return win32gui.GetWindowText(self._window)

    def _get_window_dc(self):
        hwndDC = win32gui.GetWindowDC(self._window)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        return saveDC, mfcDC, hwndDC

    def _release_window_dc(self, saveDC, mfcDC, hwndDC):
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(self._window, hwndDC)

    def __get_window_bitmap(self):
        saveDC, mfcDC, hwndDC = self._get_window_dc()
        w = self.get_window_width()
        h = self.get_window_height()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        result = windll.user32.PrintWindow(self._window, saveDC.GetSafeHdc(), 3)
        bmp_info = saveBitMap.GetInfo()
        bmp_str = saveBitMap.GetBitmapBits(True)
        self._release_window_dc(saveDC, mfcDC, hwndDC)
        img_byte_arr = io.BytesIO()
        im = Image.frombuffer(
            'RGB',
            (bmp_info['bmWidth'], bmp_info['bmHeight']),
            bmp_str, 'raw', 'BGRX', 0, 1)
        im.save(img_byte_arr, format='PNG')
        return img_byte_arr

    def get_window_bitmap(self):
        return self.__get_window_bitmap()

    def get_window_points(self):
        return win32gui.GetWindowRect(self._window)

    def get_window(self) -> int:
        return self._window

    def get_window_width(self):
        rect = self.get_window_points()
        x = rect[0]
        w = rect[2] - x
        return w

    def get_window_height(self):
        rect = self.get_window_points()
        y = rect[1]
        h = rect[3] - y
        return h


