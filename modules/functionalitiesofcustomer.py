#all the import statements are here
import os
import sys
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

class customermethods:
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def showavaiablebus(self,start_point,end_point):
        
        try:
            #variable declaration
            found_bus = False

            #open the bus json file
            with open(BUSDATABASE,"r") as file:
                bus_dic = json.load(file)

            #iterate the bus dictionary
            for bus_it in bus_dic.values():
                if(bus_it["start"].lower()==start_point.lower() and bus_it["end"].lower()==end_point.lower()):
                    print()
                    print(f"Bus id : {bus_it["id"]}")
                    print(f"Pick up point : {bus_it["start"]}")
                    print(f"Drop point point: {bus_it["end"]}")
                    print(f"Avaiable seats:{bus_it["avaiable_seats"]}")
                    print(f"Price:{bus_it["price"]}")
                    found_bus = True

            #found_bus is False then this statement will be print
            if(found_bus == False):
                print(f"Bus is not avaiable from borading point :{start_point} to drop point :{end_point}")
                
        except Exception as e:
            print(Fore.RED+f"Exception occur at Book Ticket section")
            print(f"Exception details:{e}")
            print(Style.RESET_ALL)
        
    def book_ticket(self,bus_id,no_of_seats):
        
        try:
            #all variable are declare here
            found_flag = False
            
            #open bus database json file
            with open(BUSDATABASE,"r") as file:
                bus_dic = json.load(file)
            
            #counter for generating bus database id eg."bus1"
            bus_dic_length = 0
            
            for bus_it in bus_dic.values():
                
                #bus dic counter increment by 1
                bus_dic_length = bus_dic_length + 1
                
                #generating bus database id eg."bus1"
                bus_dic_id = "bus" + str(bus_dic_length)
                
                #bus bus is found
                if(bus_it["id"]==bus_id):
                    #open book ticket json file
                    with open(BOOKTICKET,"r") as file:
                        book_dic = json.load(file)
                    
                    book_dic_length = len(book_dic)
                    
                    book_dic_id = "book"+str(book_dic_length+1)
                    
                    book_dic[book_dic_id] = {
                        "username" : self.username,
                        "id" : bus_it["id"],
                        "ticket_book" : no_of_seats,
                        "start" : bus_it["start"],
                        "end" : bus_it["end"],
                        "total_price" : bus_it["price"]*no_of_seats
                    }
                    
                    bus_dic[bus_dic_id]["avaiable_seats"] = bus_dic[bus_dic_id]["avaiable_seats"] - no_of_seats
                    
                    with open(BOOKTICKET,"w") as fileone:
                        json.dump(book_dic,fileone,indent=4)
                    with open(BUSDATABASE,"w") as filetwo:
                        json.dump(bus_dic,filetwo,indent=4)
                    print(Fore.GREEN+"Ticket Book successfully")
                    print(Style.RESET_ALL)
                    found_flag = True
                    
                    break
                
            if(found_flag == False):
                print(Fore.RED+f"Book does not book")
                print(Style.RESET_ALL)
                    
        except Exception as e:
            print(Fore.RED+f"Exception occur at Book Ticket section")
            print(f"Exception details:{e}")
            print(Style.RESET_ALL)
        
    
    def booking_details(self):
        try:
            #all variables are declare here
            found_booking = False
            
            #open booking ticket databse
            with open(BOOKTICKET,"r") as file:
                book_dic = json.load(file)
            
            for book_it in book_dic.values():
                if(self.username == book_it["username"]):
                    print(f"Start point:{book_it["start"]}")
                    print(f"End:{book_it["end"]}")
                    print(f"Number of seats booked:{book_it["ticket_book"]}")
                    print(f"Total Price of booking:{book_it["total_price"]}")
                    found_booking = True
            
            #if user does not have any booking then this file will print
            if(found_booking == False):
                print(Fore.RED+f"{self.username} does not have any booking")
                print(Style.RESET_ALL)
                
                
        except Exception as e:
            print(Fore.RED+"Exception occur at booking detaisl section")
            print(f"Exception details : {e}")
            print(Style.RESET_ALL)
    
    def functionality_of_customer(self):
        end_loop = True #variable for loop iteration
        try:
            while(end_loop):
                print()
                print("1.Avaiable bus")
                print("2.Book Ticket")
                print("3.Booking Details")
                print("4.To exit the system")
                choice = int(input("Enter your choice:"))
                match choice:
                    case 1:
                        print()
                        start_point = str(input("Enter start point:"))
                        end_point = str(input("Enter end point:"))
                        self.showavaiablebus(start_point,end_point)
                    case 2:
                        print()
                        bus_id = int(input("Enter bus id:"))
                        no_of_seats = int(input("Number of ticket:"))
                        self.book_ticket(bus_id,no_of_seats)
                    case 3:
                        print()
                        self.booking_details()
                    case _:
                        print(Fore.GREEN+f"Thank you for using our system {self.username}")
                        Style.RESET_ALL
                        end_loop = False
        except Exception as e:
            print(Fore.RED+f"Excpetion occur at functionality_of_customer methods")
            print(Fore.RED+f"Details of exceprion : {e}")
            Style.RESET_ALL