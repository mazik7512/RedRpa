import inspect
import io
import struct
import win32ui
import pywintypes
import win32con
from PIL import Image

from RRPA.Modules.CVObjectScanning.ObjectScannerGenerator import STDCVObjectScannerGenerator
from RRPA.Modules.Core.Abstract.OS.Manager.OSTools import AbstractOSTools
from RRPA.Modules.Windows.Manager.Window import STDWindow
from RRPA.Modules.Windows.Manager.WindowManager import STDWindowManager
from win32 import win32gui
from win32 import win32api


class STDOSTools(AbstractOSTools):

    scanners = {'CV': STDCVObjectScannerGenerator.generate_cv_object_scanner()}

    @staticmethod
    def create_window(win_desc):
        window = STDWindow(win_desc)
        return window

    @staticmethod
    def create_window_manager(window):
        window_manager = STDWindowManager(window, STDOSTools.scanners)
        return window_manager

    @staticmethod
    def get_windows_list():
        windows_list = []
        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windows_list)
        return windows_list

    @staticmethod
    def get_window_by_name(win_name):
        return win32gui.FindWindow(None, win_name)

    @staticmethod
    def get_window_name(win_desc):
        return win32gui.GetWindowText(win_desc)

    @staticmethod
    def get_os_tools_name():
        return STDOSTools.__name__

    @staticmethod
    def get_os_tools_import_path():
        return "RRPA.Modules.Windows.Manager.OSTools"

    @staticmethod
    def get_icon(win_desc):
        _icon = win32gui.DefWindowProc(win_desc, win32con.WM_GETICON, win32con.ICON_SMALL, 0)
        if not _icon:
            _icon = win32gui.GetClassLong(win_desc, win32con.GCL_HICON)
        if not _icon:
            return None
        res = win32gui.CopyIcon(_icon)
        icon_info = win32gui.GetIconInfo(res)
        icon = win32gui.GetObject(icon_info[3])
        #bminfo_list = []
        #bminfo_list.append(icon.bmType)
        #bminfo_list.append(icon.bmWidth)
        #bminfo_list.append(icon.bmHeight)
        #bminfo_list.append(icon.bmWidthBytes)
        #bminfo_list.append(icon.bmPlanes)
        #addr = id(icon)
        #fmt = "llllll"
        #bminfo_buf = win32gui.PyGetMemory(addr, struct.calcsize(fmt))
        #unpacked_list = struct.unpack_from(fmt, bminfo_buf)
        #print(unpacked_list)
        #for item in unpacked_list:
        #    if item not in bminfo_list:
        #        bits_addr = item
        #        break
        #print('bits_addr =', bits_addr)
        #bpp = 3
        #tot_bytes = int(icon.bmWidth * icon.bmHeight * bpp)
        #bits_str = win32gui.PyGetMemory(bits_addr, tot_bytes)
        #print(bits_str.tobytes())
        wDC = win32gui.GetDC(None)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, icon.bmHeight, icon.bmWidth)
        cDC.SelectObject(dataBitMap)
        win32gui.DrawIconEx(wDC, 0, 0, res, icon.bmHeight, icon.bmWidth, 0, None, win32con.DI_IMAGE)
        bitmap_bytes = bytearray(icon.bmHeight * icon.bmWidth * 3)
        for y in range(icon.bmHeight):
            for x in range(icon.bmWidth):
                color = win32gui.GetPixel(wDC, x, y)
                bitmap_bytes[(y * icon.bmHeight + x) * 3: (y * icon.bmWidth + x) * 3 + 3] = bytes([color & 0xFF, (color & 0xFF00) >> 8, (color & 0xFF0000) >> 16])
        bitmap_bytes = bytes(bitmap_bytes)
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(win_desc, wDC)
        win32gui.DestroyIcon(res)
        im = Image.frombuffer(
            'RGB',
            (icon.bmHeight, icon.bmWidth),
            bitmap_bytes, 'raw', 'RGB', 0, 1)
        return im

