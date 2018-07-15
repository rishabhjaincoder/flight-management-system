#Flight Management


import dl
from flight import Flight

def AddFlight():
        flightno=int(input("Enter Flight Number : "))
        name=input("Enter Flight Name : ")
        source=input("Enter Source : ")
        destination=input("Enter Destination : ")
        fare=float(input("Enter Fare : "))
        availability=""
        
        availability+=input("Sunday : ") + ","
        availability+=input("Monday : ") + ","
        availability+=input("Tuesday : ") + ","
        availability+=input("Wednesday : ") + ","
        availability+=input("Thursday : ") + ","
        availability+=input("Friday : ") + ","
        availability+=input("Saturday : ")

        flight=Flight(flightno,name,source,destination,fare,availability)
        
        if(dl.SaveFlight(flight)>0):
            print("Record Saved Successfully")
        else:
            print("Failed!")


def SearchFlight():
    flightno=int(input("Enter Flight Number : "))
    flight=dl.GetFlightDetail(flightno)
    if(flight!=None):
        print("Flight Number : " + str(flight.GetFlightNo()))
        print("Name : " + flight.GetName())
        print("Source : " + flight.GetSource())
        print("Destination : " + flight.GetDestination())
        print("Fare : " + str(flight.GetFare()))
    else:
        print("No Record Found")


def DeleteFlight():
    flightno=int(input("Enter Flight Number : "))
    if(dl.DeleteFlight(flightno)>0):
        print("Record Deleted Successfully")
    else:
        print("Record Not Found")


def UpdateFlightName():
    flightno=int(input("Enter Flight Number : "))
    name=input("Enter Flight Name : ")
    if(dl.UpdateFlightName(flightno,name)>0):
        print("Record Updated Successfully")
    else:
        print("Record Not Found")


        
def FlightMenu():
    print("1. Add New Flight")
    print("2. Update Flight Name")
    print("3. Update Flight Source")
    print("4. Update Flight Destination")
    print("5. Update Flight Fare")
    print("6. Update Flight Availability")
    print("7. Delete Flight")
    print("8. Search Flight")
    print("9. Print Flight Details")
    print("10. Check Booked Flights")
    print("11. Check Cancelled Flights")
    print("12. Update Profile")
    print("0. Exit")

    option=int(input("Enter Choice : "))

    if(option==1):
        AddFlight()
    elif(option==2):
        UpdateFlightName()
    elif(option==7):
        DeleteFlight()
    elif(option==8):
        SearchFlight()


#FlightMenu()
    


def BookingMenu():
    print("1. Book Flight")
    print("2. Check Your Bookings")
    print("3. Cancel Booking")
    print("4. Check Cancelled Bookings")
    print("5. Update Profile")

    
        



#USER

from user import User

def AddUser():
        userid=input("Enter User Id : ")
        name=input("Enter User Name : ")
        password=input("Enter Password : ")
        type=input("Enter Type (1: Admin, 0: User) : ")

        user=User(userid,name,password,type)
        
        if(dl.SaveUser(user)>0):
            print("Record Saved Successfully")
        else:
            print("Failed!")
    
def Login():
    userid=input("Enter User Id : ")
    password=input("Enter Password : ")
    user=dl.Login(userid,password)
    if(user!=None):
        if(user.GetType()==1):      #User is Admin
            FlightMenu()
        else:                       #User is User
            #BookingMenu()
            None
    else:
        print("Login Failed")


def UserMenu():
    print("1. Register")
    print("2. Login")
    print("0. Exit")

    option=int(input("Enter Choice : "))

    if(option==1):
        AddUser()
    elif(option==2):
        Login()
    elif(option==0):
        None



UserMenu()









