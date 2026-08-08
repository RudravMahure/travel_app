#all the import statements are here
import os
import sys

from colorama import  Fore,Style,init
from modules.loginsignup import searchadmin

parent_dir = os.path.abspath( os.path.join(os.path.dirname(__file__), "..") )
#the above file while first find the location os current file using "os.path.dirname(__file__)" then it go on step up
#using "os.path.join(os.path.dirname(__file__), "..")" this will give you the root folder

sys.path.append(parent_dir)

#Initialize the colorama
init()

#option of login and sign up
print("Do you want to login or sign??")
print("Press 1.Loogin")
print("Press 2.Sign up")

try:
    #taking input for choosing login or sign up
    choose_login_signup = int(input("Enter you choice:"))
    match choose_login_signup:
        case 1:
           print()
           user_name = str(input(Fore.CYAN+"Enter username:"))
           password = str(input(Fore.CYAN+"Enter password:"))
           Style.RESET_ALL
           
           check = searchadmin(user_name,password)
           print(f"value of check :{check}")
        case 2:
            print()
            user_name = str(input(Fore.CYAN+"Enter username:"))
            password = str(input(Fore.CYAN+"Enter password:"))
            repassword = str(input(Fore.CYAN+"ReEnter password:"))
            Style.RESET_ALL
        case _:
            print(Fore.RED+"Enter proper input")
            Style.RESET_ALL
except ValueError as ve:
    print(Fore.RED+f"Error occur add login section")
    print(f"Exception details : {ve}")
    Style.RESET_ALL