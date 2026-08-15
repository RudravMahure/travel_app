#all the import statements are here
import os
import sys
import random
import json

from colorama import Fore,Style,init
from config.config import BUSDATABASE
from config.config import BOOKTICKET

parent_dir = os.path.abspath( os.path.join(os.path.dirname(__file__), "..") )
#the above file while first find the location os current file using "os.path.dirname(__file__)" then it go on step up
#using "os.path.join(os.path.dirname(__file__), "..")" this will give you the root folder
sys.path.append(parent_dir)

#Initialize the colorama
init()

class adminmethods:
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    #search bus id
    def __searchbus(self,busid):
        try:
            #it checks if BUSDATABASE file exists or not
            if(os.path.exists(BUSDATABASE)):
                
                #flag to check if bus exists in BUSDATABASE or not
                bus_exists = False
                #print("inside search bus function")
                #open the BUSDATABASE json file
                with open(BUSDATABASE,"r") as file:
                    bus_dic = json.load(file)
                
                #loop to check if database has the bus id or not
                for bus_details in bus_dic.values():
                    if(bus_details["id"] == busid): 
                        bus_exists = True 
                        break
                
                #if bus id found in database function will rerturn True else false
                if(bus_exists == True):
                    return True
                else:
                    return False         
        except Exception as e:
            print(Fore.RED+"Exception occur at search bus method")
            print(f"Exception details : {e}")
            print(Style.RESET_ALL)
     
     
    #add bus into json file       
    def __addbus(self):    
        try:
            bus_id = random.randint(1,100)   
            unique_id_flag = True
            
            #this loop will run till its generate a unique bus id
            while(unique_id_flag):            
                unique_id_flag = self.__searchbus(bus_id)
                
                if (unique_id_flag == True):
                    bus_id = random.randint(1,100)
                    self.__searchbus(bus_id)
                    
            
            start_point = str(input(Fore.CYAN+"Enter the starting point of bus:"))
            end_point = str(input("Enter the ending point of bus:"))
            total_seats = int(input("Enter total number of seats:"))
            price = int(input("Enter the price of each seat:"))
            print(Style.RESET_ALL)
            
            start_point = start_point.lower()
            end_point = end_point.lower()
            
            #check if bus path exists or not
            if(os.path.exists(BUSDATABASE)):
                #open the BUSDATABASE json file
                with open(BUSDATABASE,"r") as file:
                    bus_dic = json.load(file)

                bus_dic_length = len(bus_dic)
                bus_dic_id = "bus"+str(bus_dic_length+1) 
                
                #new entry for dictionary
                bus_dic[bus_dic_id] = {
                    "id" : bus_id,
                    "start" : start_point,
                    "end" : end_point,
                    "total_seats" : total_seats,
                    "avaiable_seats" : total_seats,
                    "price" : price
                }   
                #write into json file
                with open(BUSDATABASE,"w") as file:
                    json.dump(bus_dic,file,indent=4)
                
                print(Fore.GREEN+"Bus Added successfully")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED+"Json file does not found")
                print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+f"Exception occur at add bus method")
            print(f"Exception details : {e}")
            print(Style.RESET_ALL)
        
    
    def __showbus(self):
        try:
            if(os.path.exists(BUSDATABASE)):
                
                #open BUSDATABASE file
                with open(BUSDATABASE,"r") as file:
                    bus_dic = json.load(file)
                
                print(Fore.CYAN+"All the Bus Details")
                print(Style.RESET_ALL)
                #printing bus details
                for bus_details in bus_dic.values():
                    print()
                    print(f"Bus id:{bus_details["id"]}")
                    print(f"Starting point:{ bus_details["start"]}")
                    print(f"Ending point:{bus_details["end"]}")
                    print(f"Total seats:{bus_details["total_seats"]}")
                    print(f"Avaiable seats:{bus_details["avaiable_seats"]}")
                    print(f"The price of each seat:{bus_details["price"]}")
            else:
                print(Fore.RED+"Json File does not found")
                print(Style.RESET_ALL)
                   
        except Exception as e:
            print(Fore.RED+f"Exception occur at show bus method")
            print(f"Exception Details : {e}")
            print(Style.RESET_ALL)  
    
    #delete bus method    
    def __deletebus(self,bus_id):
        try:
            if(os.path.exists(BUSDATABASE)):
                #open the BUSDATABASE file in read mode
                with open(BUSDATABASE,"r") as file:
                    bus_dic = json.load(file)
                
                found_bus_flag = False
                
                temp_dic_length = 1
                bus_dic_length = 1
                
                temp_dic = {}
                bus_dic_id = "bus"+str(bus_dic_length)
                
                #loop to delete the bus in BUSDATABASE
                for bus_details in bus_dic.values():
                    if(bus_id != bus_details["id"]):
                        
                        temp_dic_id = "bus"+str(temp_dic_length)
                        temp_dic[temp_dic_id] = {
                            "id" : bus_dic[bus_dic_id]["id"],
                            "start" : bus_dic[bus_dic_id]["start"],
                            "end" : bus_dic[bus_dic_id]["end"],
                            "total_seats" : bus_dic[bus_dic_id]["total_seats"],
                            "avaiable_seats" : bus_dic_id["avaiable_seats"],
                            "price" : bus_dic[bus_dic_id]["price"]
                        }
                        temp_dic_length = temp_dic_length + 1
                        
                    else:
                        found_bus_flag = True 
                       
                    bus_dic_length = bus_dic_length + 1
                    bus_dic_id = "bus"+str(bus_dic_length)
                
                if(found_bus_flag == True):
                    with open(BUSDATABASE,"w") as file:
                        json.dump(temp_dic,file,indent=4)
                    print(Fore.GREEN+f"Bus Delete Successful")
                    print(Style.RESET_ALL)
                else:
                    print()
                    print(Fore.RED+f"Bus does not found")
                    print(Style.RESET_ALL)
            else:
                print(Fore.RED+"Json file does not exits")
                print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+f"Exception occur at delete bus section")
            print(f"Exception details : {e}")
            print(Style.RESET_ALL)
    
    def __updatedetails(self,bus_id,change_value,updated_value):
            try:
                #check if bus database json file exists or not
                if(os.path.exists(BUSDATABASE)):
                    
                    bus_dic_flag = False
                    #opening BUSDATABASE file
                    with open(BUSDATABASE,"r") as file:
                        bus_dic = json.load(file)
                    
                    bus_dic_length = 1
                    
                    for bus_details in bus_dic.values():
                        bus_dic_id = "bus"+str(bus_dic_length)
                        
                        if(bus_id==bus_details["id"]):
                            bus_dic[bus_dic_id][change_value] = updated_value
                            bus_dic_flag = True
                            
                            print(Fore.GREEN+f"Update done successfully")
                            print(Style.RESET_ALL)
                            
                        bus_dic_length = bus_dic_length + 1
                        
                    if(bus_dic_flag == True):
                        with open(BUSDATABASE,"w") as file:
                            json.dump(bus_dic,file,indent=4)
                    
                else:
                    print(Fore.RED+f"Json file does not found")
                    print(Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED+f"Exception occur at update details method")
                print(f"Exception details : {e}")
                print(Style.RESET_ALL)
    
    #total earning function
    def total_earning(self):
        
        #all variables are declare here
        v_total_earning = 0
        
        try:
            with open(BOOKTICKET,"r") as file:
                book_dic = json.load(file)
            
            for book_it in book_dic.values():
                v_total_earning = v_total_earning + book_it["total_price"]
            
            print()
            print(f"Total earning:{v_total_earning}")
                
        except Exception as e:
            print(Fore.RED+"Exception occur at total earning section")
            print(f"Exception details : {e}")
            print(Style.RESET_ALL)
    
    #match case
    def functionality_of_admin(self):
        end_loop = True #variable for loop iteration
        try:
            while(end_loop):
                print()
                print("1.Add bus")
                print("2.Delete bus")
                print("3.Update bus Details")
                print("4.Total Earning")
                print("5.Show all bus")
                print("6.To exit the system")
                choice = int(input("Enter your choice:"))
                match choice:
                    case 1:
                        print(Fore.CYAN+f"Add bus")
                        print(Style.RESET_ALL)
                        self.__addbus()
                    case 2:
                        print(Fore.CYAN+"Delete Bus Section")
                        print(Style.RESET_ALL)
                        bus_id = int(input("Enter bus id:"))
                        self.__deletebus(bus_id)
                    case 3:
                        print(Fore.CYAN+f"Update bus Details")
                        print(Style.RESET_ALL)
                        
                        bus_id = int(input("Enter bus id:"))
                        print("What you want to change?")
                        print("1.Change starting point")
                        print("2.Change ending point")
                        print("3.Change total seats")
                        print("4.Change price")
                        print("5.Avaiable seats")
                        
                        choice = int(input("Enter your choice:"))
                        if(choice == 1):
                            change_value = "start"
                            updated_value = str(input("Enter new start location:"))
                        elif(choice == 2):
                            change_value = "end"
                            updated_value = str(input("Enter new end location:"))
                        elif(choice == 3):
                            change_value = "total_seats"
                            updated_value = int(input("Enter new total seats:"))
                        elif(choice == 4):
                            change_value = "price"
                            updated_value = int(input("Enter new price:"))
                        elif(choice == 5):
                            change_value = "avaiable_seats"
                            updated_value = int(input("Enter new avaiable seats:"))
                        else:
                            print(Fore.RED+f"Enter proper input")
                            print(Style.RESET_ALL)
                        self.__updatedetails(bus_id,change_value,updated_value)
                        
                    case 4:
                        print("Total earning")
                        self.total_earning()
                    case 5:
                        print("Show all bus")
                        self.__showbus()
                    case _:
                        print(Fore.GREEN+f"Thank you for using our system {self.username}")
                        print(Style.RESET_ALL)
                        end_loop = False
        except Exception as e:
            print(Fore.RED+f"Excpetion occur at functionality_of_admin methods")
            print(Fore.RED+f"Details of exceprion : {e}")
            print(Style.RESET_ALL)

