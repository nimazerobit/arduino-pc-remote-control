import win32api
import win32con
from colorama import Fore, Style

class F_Button:
    def f(self, number):
        vk_code = getattr(win32con, f"VK_F{number}", None)
        if vk_code:
            win32api.keybd_event(vk_code, 0)
            win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP)
        else:
            print(Fore.RED + "[-] Error: Invalid function key number." + Style.RESET_ALL)
            