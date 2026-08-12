#all the import statements are here
import os
import sys

from colorama import Fore,Style,init

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
    
    def functionality_of_admin(self):
        end_loop = True #variable for loop iteration
        try:
            while(end_loop):
                print()
                print("1.Add bus")
                print("2.Delete bus")
                print("3.Update bus Details")
                print("4.Total Earning")
                print("5.To exit the system")
                choice = str(input("Enter your choice:"))
                match choice:
                    case 1:
                        print("Add bus")
                    case 2:
                        print("Delete")
                    case 3:
                        print("Update bus Details")
                    case 4:
                        print("Total earning")
                    case _:
                        print(Fore.GREEN+f"Thank you for using our system {self.username}")
                        Style.RESET_ALL
                        end_loop = False
        except Exception as e:
            print(Fore.RED+f"Excpetion occur at functionality_of_admin methods")
            print(Fore.RED+f"Details of exceprion : {e}")
            Style.RESET_ALL