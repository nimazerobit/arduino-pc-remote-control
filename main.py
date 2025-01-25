import serial
import os
from dotenv import load_dotenv
import time
import json
from colorama import Fore, Back, Style
from modules import action_handler

# load environment variables
load_dotenv()
arduino_port = os.getenv("ARDUINO_PORT")
baud_rate = int(os.getenv("BAUD_RATE"))
version_number = os.getenv("VERSION")
remote_map_file = os.getenv("REMOTE_MAP_FILE")

# clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# print banner
def print_banner():
    print(Fore.CYAN +f"""
    ___             __      _                ____                       __     
   /   |  _________/ /_  __(_)___  ____     / __ \\___  ____ ___  ____  / /____ 
  / /| | / ___/ __  / / / / / __ \\/ __ \\   / /_/ / _ \\/ __ `__ \\/ __ \\/ __/ _ \\
 / ___ |/ /  / /_/ / /_/ / / / / / /_/ /  / _, _/  __/ / / / / / /_/ / /_/  __/
/_/  |_/_/   \\__,_/\\__,_/_/_/ /_/\\____/  /_/ |_|\\___/_/ /_/ /_/\\____/\\__/\\___/ 
Arduino PC Remote Control | By @nimazerobit | Version {version_number}                                                                            
    """ + Style.RESET_ALL)
    for i in range(0, 40): # print line
        print(Fore.YELLOW + "-_" , end="")
    print(Style.RESET_ALL + "\n")

# connect to arduino
def connect_arduino():
    global ser # make ser variable global
    while True: # try to connect to arduino until connected
        try:
            ser = serial.Serial(arduino_port, baud_rate, timeout=1) # connect to arduino
            print(Fore.GREEN + f"\r[+] Connected to Arduino on {arduino_port}{30*" "}\n" + Style.RESET_ALL, end="")
            break
        except Exception:
            animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"] # animation array
            for i in animation: # play animation
                print(Fore.RED + f"\r[-] ERROR: Please connect the board. Checking for connection {i}", end="")
                time.sleep(0.1)

# remote code receiver
def remote_code_receiver():
    if not os.path.exists(remote_map_file):
        print(Fore.RED + f"[-] Error: '{remote_map_file}' file not found." + Style.RESET_ALL)
        return

    try:
        with open(remote_map_file) as f: # open remote map file
            remote_config = json.load(f)

        while True:
            try:
                data = ser.readline().decode('utf-8').strip()
                if data not in ["FFFFFFFF", ""]:  # skip if button is holding
                    # find the action for the received code
                    action = next((btn['action'] for btn in remote_config.values() if btn['code'] == data), None)
                    print(Fore.LIGHTBLUE_EX + f"[*] Received code: {Fore.YELLOW + data + Fore.LIGHTBLUE_EX} | Action: {Fore.YELLOW + action + Fore.LIGHTBLUE_EX}" + Style.RESET_ALL)
                    action_handler.action_handler(action) # handle the action

            except KeyboardInterrupt:
                print(Fore.RED + "[-] Exiting..." + Style.RESET_ALL)
                break
            except Exception as e:
                print(Fore.RED + f"[-] Error: {e}" + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + f"[-] Error: '{remote_map_file}' not found." + Style.RESET_ALL)

# main function
def main():
    clear_console()
    print_banner()
    print(Fore.LIGHTBLUE_EX + f"[*] Checking for Arduino on {arduino_port} at {baud_rate} baud rate..." + Style.RESET_ALL)
    connect_arduino() # connect to arduino
    remote_code_receiver() # receive remote codes

main()