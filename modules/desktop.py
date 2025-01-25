from pyvda import VirtualDesktop, get_virtual_desktops

class WindowsDesktop:
    def switch_desktop(self, number):
        number_of_active_desktops = len(get_virtual_desktops())
        if number_of_active_desktops >= number:
            VirtualDesktop(number).go()
        else:
            print(f"There are {number_of_active_desktops} active desktops")

    def add_desktop(self):
        try:
            VirtualDesktop.create()
            number_of_active_desktops = len(get_virtual_desktops())
            VirtualDesktop(number_of_active_desktops).go()
            print("New virtual desktop created and switched.")
        except Exception as e:
            print(f"Error creating or switching to a new desktop: {e}")