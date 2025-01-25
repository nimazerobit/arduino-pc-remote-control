from modules import media
from modules import f_button
from modules import desktop
from modules import windows

media = media.Media()
f_button = f_button.F_Button()
windesktop = desktop.WindowsDesktop()
windows = windows.Windows()

def action_handler(action):
    if action:
        # None action
        if action == "none":
            return
        
        # Media
        elif action == "PLAY_PAUSE":
            media.play_pause()
        elif action == "NEXT_TRACK":
            media.next()
        elif action == "PREVIOUS_TRACK":
            media.previous()
        elif action == "VOLUME_UP":
            media.volume_up()
        elif action == "VOLUME_DOWN":
            media.volume_down()
        elif action == "VOLUME_MUTE":
            media.volume_mute()
        
        # Windows
        elif action == "SHUTDOWN":
            windows.shutdown()
        elif action == "LOCK":
            windows.lock()

        # Windows Desktop
        elif action == "ADD_DESKTOP":
            windesktop.add_desktop()
        elif action.startswith("SWITCH_DESKTOP"):
            desktop_number = int(action.split("_")[-1])
            windesktop.switch_desktop(desktop_number)

        # F Button
        elif action.startswith("F_BUTTON"):
            button_number = int(action.split("_")[-1])
            f_button.f(button_number)