import win32con
import win32api

class Media:
    def play_pause(self):
        hwcode = win32api.MapVirtualKey(win32con.VK_MEDIA_PLAY_PAUSE, 0)
        win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, hwcode)

    def next(self):
        win32api.keybd_event(win32con.VK_MEDIA_NEXT_TRACK, 0, 0, 0)
        win32api.keybd_event(win32con.VK_MEDIA_NEXT_TRACK, 0, win32con.KEYEVENTF_KEYUP, 0)

    def previous(self):
        win32api.keybd_event(win32con.VK_MEDIA_PREV_TRACK, 0, 0, 0)
        win32api.keybd_event(win32con.VK_MEDIA_PREV_TRACK, 0, win32con.KEYEVENTF_KEYUP, 0)

    def volume_up(self):
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0)
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_KEYUP)

    def volume_down(self):
        win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0)
        win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0, win32con.KEYEVENTF_KEYUP)

    def volume_mute(self):
        win32api.keybd_event(win32con.VK_VOLUME_MUTE, 0)
        win32api.keybd_event(win32con.VK_VOLUME_MUTE, 0, win32con.KEYEVENTF_KEYUP)
    