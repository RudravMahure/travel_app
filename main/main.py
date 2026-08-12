#all the import statements are here
import os
import sys

from colorama import  Fore,Style,init
from modules.loginsignup import searchadmin
from modules.loginsignup import searchcustomer
from modules.loginsignup import entry_of_new_customer
from modules.functionalitiesofcustomer import customermethods
from modules.functionalitiesofadmin import adminmethods

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
           print(Style.RESET_ALL)
           
           checkuser = searchcustomer(user_name,password)
           checkadmin = searchadmin(user_name,password)
           
           if(checkuser == True and checkadmin == False):
               print("functionalities of customer")
               customer_credintails = customermethods(user_name,password)
               customer_credintails.functionality_of_customer()
           elif(checkadmin == True and checkuser == False):
               admin_credintails = adminmethods(user_name,password)
               admin_credintails.functionality_of_admin()
           else:
               print(Fore.RED+f"Incorrect username or password \nusername doesnot exist")
               print(Style.RESET_ALL)
            
               
        case 2:
            print()
            user_name = str(input(Fore.CYAN+"Enter username:"))
            password = str(input(Fore.CYAN+"Enter password:"))
            repassword = str(input(Fore.CYAN+"ReEnter password:"))
            print(Style.RESET_ALL)
            if(password==repassword):
                entry_of_new_customer(user_name,password)
            else:
                print(Fore.RED+f"Password and reenter pasword does not match")
                print(Style.RESET_ALL)
        case _:
            print(Fore.RED+"Enter proper input")
            print(Style.RESET_ALL)
except ValueError as ve:
    print(Fore.RED+f"Error occur add login section")
    print(f"Exception details : {ve}")
    Style.RESET_ALL