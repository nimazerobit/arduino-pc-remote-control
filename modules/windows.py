import subprocess

class Windows:
    def shutdown(self):
        subprocess.run(["shutdown", "/s", "/f", "/t", "0"])

    def lock(self):
        subprocess.run("rundll32.exe user32.dll,LockWorkStation")
        