import win32con
import win32gui


class WindowActionizer:
    @staticmethod
    def close(hwnd: int):
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE)

    @staticmethod
    def focus(hwnd: int):
        win32gui.SetForegroundWindow(hwnd)
        win32gui.SetActiveWindow(hwnd)

    @staticmethod
    def move(hwnd: int, x: int, y: int, width: int, height: int, repaint=True):
        win32gui.MoveWindow(hwnd, x, y, width, height, repaint)
