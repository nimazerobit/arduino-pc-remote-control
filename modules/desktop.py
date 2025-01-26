from pyvda import VirtualDesktop, get_virtual_desktops
from colorama import Fore, Style

class WindowsDesktop:
    def switch_desktop(self, number):
        number_of_active_desktops = len(get_virtual_desktops())
        if number_of_active_desktops >= number:
            VirtualDesktop(number).go()
        else:
            print(Fore.RED + "[-] Error: Desktop number out of range." + Style.RESET_ALL)

    def add_desktop(self):
        try:
            VirtualDesktop.create()
            number_of_active_desktops = len(get_virtual_desktops())
            VirtualDesktop(number_of_active_desktops).go()
            print(Fore.GREEN + f"[+] New virtual desktop created" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "[-] Error: Could not create a new desktop." + Style.RESET_ALL)