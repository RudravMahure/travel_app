#all import statements are here
from config.config import ADMIN_DATABASE
from config.config import CUSTOMER_DATABASE
from colorama import Fore,Style,init

import json

#Initialize the colorama
init()

#this method will first check the user is admin or not
def searchadmin(username,password):
    
    try:
        #all variable are declare here
        found_user = False
        incorrect_password = True
        
        #opening admin json file
        with open(ADMIN_DATABASE,"r") as file:
            admincheck = json.load(file)
        
        #loop to check if admin or not\
        for check in admincheck.values():
            if(check["username"]==username):
                found_user = True
                if(check["username"]==username and check["password"]==password):
                    incorrect_password = False
                    break
                elif(check["username"]==username and check["password"]==password):
                    incorrect_password = True
                    break
            else:
                found_user = False
        
        #return statement
        if(found_user == False):
            print(Fore.RED+"Incorrect username of username does not exists")
            Style.RESET_ALL
            return False
        elif(found_user == True and incorrect_password == False):
            return True
        elif(found_user == True and incorrect_password == True):
            print(Fore.RED+"Incorrect Password")
            Style.RESET_ALL
            return False
    except Exception as e:
        print(Fore.RED+"Exception occur at search admin method")
        print(Fore.RED+f"Exception details :{e}")
        Style.RESET_ALL