import os
import eauth
from datetime import datetime
import platform
import time
import sys

# Init request
if (not eauth.init_request()):
    print(eauth.error_message)
    time.sleep(1.5)
    sys.exit(0)

# Pause command
def run_pause_command():
    if platform.system() == 'Windows':
        os.system('pause')
    else:
        input('Press Enter to continue...')

def main_f():
    os.system('cls')
    print("▒█▀▀▀ ░█▀▀█ ▒█░▒█ ▀▀█▀▀ ▒█░▒█ ")
    print("▒█▀▀▀ ▒█▄▄█ ▒█░▒█ ░▒█░░ ▒█▀▀█ ")
    print("▒█▄▄▄ ▒█░▒█ ░▀▄▄▀ ░▒█░░ ▒█░▒█")
    print(" ")
    print(" ")
    print("[ 1 ] Login     [ 2 ] Register")
    print(" ")
    print("[?]",end=" ")
    value = input("user@eauth:~$ ")
    if value == "1":
        os.system('cls')
        username = input("Username: ")
        password = input("Password: ")
        if (eauth.login_request(username, password)):
            os.system('cls')
            print("You are logged in!")
            print(" ")
            print("Rank: " + eauth.rank)
            print("Create Date: " + eauth.register_date)
            print("Expire Date: " + eauth.expire_date)
            print("Hardware ID: " + eauth.user_hwid)
        else:
            print(eauth.error_message)
        time.sleep(3)
        main_f()
    elif value == "2":
        os.system('cls')
        username = input("Username: ")
        password = input("Password: ")
        invite = input("License Key: ")
        if (eauth.register_request(username, password, invite)):
            os.system('cls')
            print("You are registered!")
        else:
            print(eauth.error_message)
        time.sleep(1.5)
        main_f()
    else:
        os.system('cls')
        print("Invalid input!")
        time.sleep(1)
        main_f()

main_f()
run_pause_command()