import random
import string
import subprocess
import os
from getpass import getpass

def clear_screen():
    if os.name == 'nt':  # For Windows
        subprocess.run(['cls'], shell=True)
    else:  # For Unix/Linux/Mac
        subprocess.run(['clear'])
clear_screen()

user_pass = {}

def sign_up():
    global user_pass
    if not user_pass:
        while True:
            username = input("Enter a username: ")
            if username.strip():
                break
            else:
                print("Username cannot be empty. Please try again.")
    
        while True:
            password = getpass("Enter a password: ")
            if len(password) >= 6:
                re_password = getpass("Re-enter your password to confirm: ")
                if password == re_password:
                    clear_screen()
                    print('Signed up')
                    user_pass[username] = password
                    break
                else:
                    print("You entered the wrong confirmation password. Please try again.")
            else:
                print("Password should be at least 6 characters long. Please try again.")
    
    else:
        while True:
            username = input("Enter a username: ")
            if username not in user_pass:
                if username.strip():
                    break
                else:
                    print("Username cannot be empty. Please try again.")
            else:
                print('This username already exist')
    
        while True:
            password = getpass("Enter a password: ")
            if len(password) >= 6:
                re_password = getpass("Re-enter your password to confirm: ")
                if password == re_password:
                    clear_screen()
                    print('Signed up')
                    user_pass[username] = password
                    break
                else:
                    clear_screen()
                    print("You entered the wrong confirmation password. Please try again.")
            else:
                clear_screen()
                print("Password should be at least 6 characters long. Please try again.")
                

def login(system):
    while True:
        username1 = input("Enter your username: ")
        if username1 in system.keys():
            print("Now enter your password:")
            password1 = getpass("Password: ")
            if password1 == system[username1]:
                clear_screen()
                print("Logged in")
                break
            else:
                clear_screen()
                print("Wrong password. Please try again.")
        else:
            clear_screen()
            print("Wrong username. Please try again.")
            
def captcha_system():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(6))

def psw(reset):
    if not reset:
        clear_screen()
        print("No users to reset password.")
        return
    
    username3 = input("Enter your username: ")
    if username3 in reset:
        correct_word = captcha_system()
        clear_screen()
        print("Please type the word:", correct_word)
        user_input = input("Enter the word: ")
        
        if user_input == correct_word:
            print("You're not a robot.")
            while True:
                password3 = getpass("Enter a new password: ")
                if len(password3) >= 6:
                    if password3 != reset[username3]:
                        re_password1 = getpass("Re-enter your password to confirm: ")
                        if password3 == re_password1:
                            reset[username3] = password3
                            clear_screen()
                            print("Password reset successfully.")
                            break
                        else:
                            print("You entered the wrong confirmation password. Please try again.")
                    else:
                        print("Your new password must be different from the old one.")
                else:
                    print("Password must be at least 6 characters long.")
        else:
            print("CAPTCHA failed! You might be a robot.")
    else:
        clear_screen()
        print("Username not found. Can't reset password.")


while True:
    print("Choice\n 1. To sign Up\n 2. To login\n 3. To reset password\n 4. To Exit")
    choose = input("Choose 1, 2, 3, or 4: ")
    if choose == "1":
        sign_up()
    elif choose == "2":
        if user_pass:
            login(user_pass)
        else:
            print("You need to sign up first.")
    elif choose == "3":
        psw(user_pass)
    elif choose == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice. Please choose again.")
