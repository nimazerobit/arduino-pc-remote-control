import win32api
import win32con

class F_Button:
    def f(self, number):
        vk_code = getattr(win32con, f"VK_F{number}", None)
        if vk_code:
            win32api.keybd_event(vk_code, 0)
            win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP)
        else:
            print("Invalid function key number. Use a number between 1 and 24.")