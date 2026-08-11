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
            #print(Fore.RED+"Incorrect username or username does not exists")
            print(Style.RESET_ALL)
            return False
        elif(found_user == True):
            #print(Fore.GREEN+f"WElcome to system")
            print(Style.RESET_ALL)
            return True
        
    except Exception as e:
        print(Fore.RED+"Exception occur at search admin method")
        print(Fore.RED+f"Exception details :{e}")
        print(Style.RESET_ALL)
        
#this method will check if user is customer
def searchcustomer(username,password):
    try:
        #all variables are declare here
        found_user = False
        incorrect_password = False
        
        #open the customer file
        with open(CUSTOMER_DATABASE,"r") as file:
            customer_dic = json.load(file)
            
        #loop to iterate the user
        for check in customer_dic.values():
            if(check["username"]==username):
                if(check["password"]==password):
                    found_user = True
                    incorrect_password = False
                    break
                else:
                    found_user = True
                    incorrect_password = True
                    break
        
        if(found_user == False):
            #print(Fore.RED+f"Incorrect username or username does not exist")
            print(Style.RESET_ALL)
            return False
        elif(found_user == True):
            #print(Fore.GREEN+f"Welcome to the system")
            print(Style.RESET_ALL)
            return True
        
        
    except Exception as e:
        print(Fore.RED+"Exception occur at search user method")
        print(Fore.RED+f"Details of exception: {e}")
        print(Style.RESET_ALL)

def entry_of_new_customer(username,password):
    try:
        #open the customer json file in read mode to get data
        with open(CUSTOMER_DATABASE,"r") as fileone:
            customer_dic = json.load(fileone)
        
        if(searchcustomer(username,password)==True):
            print(Fore.RED+f"User already exists")
            return False
        else:
            
            customer_dic_length = len(customer_dic)
            customer_dic_length = customer_dic_length + 1
            
            customer_id = str("cust")+str(customer_dic_length)
            
            customer_dic[customer_id] = {
                "username":username,
                "password":password
            }
            
            #json file is open to add new customer into json file
            with open(CUSTOMER_DATABASE,"w") as filetwo:
                json.dump(customer_dic,filetwo,indent=4)
            
            print(Fore.GREEN+"Customer added successfully")
            print(Style.RESET_ALL)
            return True
        
    except Exception as e:
        print(Fore.RED+f"Exception occur at entry of new customer method")
        print(Fore.RED+f"Exception details: {e}")
        print(Style.RESET_ALL)
        