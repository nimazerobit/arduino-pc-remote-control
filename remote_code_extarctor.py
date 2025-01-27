import sys
import serial
import os
import time
import inquirer
from dotenv import load_dotenv
from colorama import Fore, Back, Style
import json
from datetime import datetime

# load environment variables
if not os.path.exists(".env"): # create .env file if not exists
    with open(".env", "w") as f:
        f.write("ARDUINO_PORT=COM3\nBAUD_RATE=9600\nVERSION=1.0\nREMOTE_MAP_FILE=remote_map.json")
        print(Fore.YELLOW + "[!] .env file created. Please configure the file before running the program." + Style.RESET_ALL)
        exit()
load_dotenv()
arduino_port = os.getenv("ARDUINO_PORT")
baud_rate = int(os.getenv("BAUD_RATE"))
version_number = os.getenv("VERSION")

# variables
warning_message = Fore.YELLOW + "[!] Warning: Please" + Fore.RED + " do not " + Fore.YELLOW + "eject the Arduino while the program is running.\n" + Style.RESET_ALL

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

# app menu
def menu():
    options = ["Remote Code Receiver 1", "Remote Code Receiver 2", "Exit"] # menu options
    question = [inquirer.List('choice', message="Select an option", choices=options)] # menu question
    answer = inquirer.prompt(question) # get user choice
    return options.index(answer['choice']) # return user choice index (index starts from 0)

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

# remote code receiver 1
def remote_code_receiver_1():
    print(warning_message) # print warning message
    print(Fore.LIGHTBLUE_EX + f"[*] Waiting for remote code...\n" + Style.RESET_ALL)
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            if data not in ["FFFFFFFF", ""]: # don't print if button is holding
                print(Fore.LIGHTBLUE_EX + f"[*] Button Code: " + Back.YELLOW + Fore.BLACK + data + Style.RESET_ALL)
        except KeyboardInterrupt:
            break
        except Exception:
            pass

# remote code receiver 2
def remote_code_receiver_2():
    button_codes = [] # button codes array
    print(warning_message) # print warning message
    while True: # get remote button count from user
        try:
            remote_button_count = int(input(Fore.LIGHTBLUE_EX + f"[?] Enter your remote button count : " + Style.RESET_ALL)) # get remote button count from user
            break
        except ValueError:
            print(Fore.RED + f"[-] Please enter a valid number" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + f"\n[*] Capturing Codes...\n" + Style.RESET_ALL)
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            if data not in ["FFFFFFFF", ""] and data not in button_codes:
                button_codes.append(data)
                print(Fore.LIGHTBLUE_EX + f"[{len(button_codes)}] Button Code: " + Back.YELLOW + Fore.BLACK + data + Style.RESET_ALL)
                if len(button_codes) == remote_button_count:
                    break
        except KeyboardInterrupt:
            break
        except Exception:
            pass

    if len(button_codes) != 0: # check if codes are captured
        print(Fore.GREEN + f"\n[*] Codes Captured Successfully\n" + Style.RESET_ALL)
        ask_save = input(Fore.LIGHTBLUE_EX + f"[?] Do you want to save the codes to a file? (y/n) : " + Style.RESET_ALL)
        if ask_save.lower() == "y": # save codes to file if user wants
            file_name = input(Fore.LIGHTBLUE_EX + f"[?] Enter the file name (without extension) : " + Style.RESET_ALL)
            if file_name == "": # set default file name if empty
                file_name = "remote_codes_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            if not file_name.endswith(".json"): # add .json extension if not provided
                file_name = file_name + ".json"
            button_data = {f"button{i+1}": {"code": code, "action": "none"} for i, code in enumerate(button_codes)}
            with open(file_name, "w") as file:
                json.dump(button_data, file, indent=4)
            print(Fore.GREEN + f"\n[*] Codes saved to {file_name}\n" + Style.RESET_ALL)
            input(Fore.LIGHTBLUE_EX + f"[?] Press any key to continue..." + Style.RESET_ALL)
    else:
        print(Fore.RED + f"\n[-] No codes captured\n" + Style.RESET_ALL)
        input(Fore.LIGHTBLUE_EX + f"[?] Press any key to continue..." + Style.RESET_ALL)


# main function
def main():
    first_time_menu = True # set first time menu to True
    try:
        clear_console()
        print_banner()
        print(Fore.LIGHTBLUE_EX + f"[*] Checking for Arduino on {arduino_port} at {baud_rate} baud rate..." + Style.RESET_ALL)

        connect_arduino() # connect to arduino
        print(warning_message) # print warning message

        while True:
            if first_time_menu == False: # clear console if it's not the first time
                clear_console()
                print_banner()
                print(warning_message)

            user_choice = menu() # show menu
            first_time_menu = False # set first time menu to False

            if user_choice == 0:
                clear_console()
                print_banner()
                remote_code_receiver_1()

            elif user_choice == 1:
                clear_console()
                print_banner()
                remote_code_receiver_2()

            elif user_choice == 2:
                print(Fore.RED + "[-] Exiting..." + Style.RESET_ALL)
                if 'ser' in globals() and ser.is_open: # close serial connection if open
                    ser.close()
                time.sleep(1)
                sys.exit(0)


    except KeyboardInterrupt:
        print(Fore.RED + "\n[-] Program terminated by user" + Style.RESET_ALL)
        if 'ser' in globals() and ser.is_open: # close serial connection if open
            ser.close()
        sys.exit(0)

# run the program
main()