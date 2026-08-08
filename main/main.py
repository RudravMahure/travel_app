#all the import statements are here
import os
import sys

parent_dir = os.path.abspath( os.path.join(os.path.dirname(__file__), "..") )
#the above file while first find the location os current file using "os.path.dirname(__file__)" then it go on step up
#using "os.path.join(os.path.dirname(__file__), "..")" this will give you the root folder

sys.path.append(parent_dir )

#option of login and sign up
print("Do you want to login or sign??")
print("Press 1.Loogin")
print("Press 2.Sign up")

try:
    #taking input for choosing login or sign up
    choose_login_signup = int(input("Enter you choice:"))
    match choose_login_signup:
        case 1:
        
        case 2:
        
        case _:
except ValueError as ve:
    print("")