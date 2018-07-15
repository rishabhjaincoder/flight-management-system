#Database Logic (DL)

#Global Variables

import MySQLdb

con=MySQLdb.connect('localhost',user='root',password='')
con.select_db('fms')




#Flight Module

from flight import Flight

def SaveFlight(flight):
    cur=con.cursor()
    result=cur.execute("INSERT INTO FLIGHT (flightno,name,source,destination,fare,availability) values(%s,%s,%s,%s,%s,%s)",(flight.GetFlightNo(),flight.GetName(),flight.GetSource(),flight.GetDestination(),flight.GetFare(),flight.GetAvailability()))
    con.commit()
    return result


def DeleteFlight(flightno):
    cur=con.cursor()
    result=cur.execute("DELETE FROM FLIGHT WHERE flightno="+str(flightno))
    con.commit()
    return result


def UpdateFlightName(flightno,name):
    cur=con.cursor()
    result=cur.execute("UPDATE FLIGHT SET name=%s WHERE FLIGHTNO=%s",(name,flightno))
    con.commit()
    return result


def GetFlightDetails():
    cur=con.cursor()
    cur.execute("SELECT * FROM FLIGHT")
    data=con.fetchall()

    flights=[]
    for record in data:
        flight=Flight(data[0],data[1],data[2],data[3],data[4],data[5])
        flights.append(flight)
    return flights
    

def GetFlightDetail(flightno):
    cur=con.cursor()
    cur.execute("SELECT * FROM FLIGHT WHERE flightno="+str(flightno))
    data=cur.fetchone()

    if(data==None):
        return None
    
    flight=Flight(data[0],data[1],data[2],data[3],data[4],data[5])
    return flight   



#User Module

from user import User

def SaveUser(user):
    cur=con.cursor()
    result=cur.execute("INSERT INTO USER (userid,name,password,type) values(%s,%s,%s,%s)",(user.GetUserId(),user.GetName(),user.GetPassword(),user.GetType()))
    con.commit()
    return result


def DeleteUser(userid):
    cur=con.cursor()
    result=cur.execute("DELETE FROM USER WHERE userid="+userid)
    con.commit()
    return result


def UpdateUserName(userid,name):
    cur=con.cursor()
    result=cur.execute("UPDATE USER SET name=%s WHERE userid=%s",(name,userid))
    con.commit()
    return result


def GetUserDetails():
    cur=con.cursor()
    cur.execute("SELECT * FROM USER")
    data=con.fetchall()

    users=[]
    for record in data:
        user=User(data[0],data[1],data[2],data[3])
        users.append(user)
    return users
    

def GetUserDetail(userid):
    cur=con.cursor()
    cur.execute("SELECT * FROM USER WHERE userid="+userid)
    data=cur.fetchone()

    if(data==None):
        return None
    
    user=User(data[0],data[1],data[2],data[3])
    return user   
    

def Login(userid,password):
    cur=con.cursor()
    cur.execute("SELECT * FROM USER WHERE userid=%s and password=%s",(userid,password))
    data=cur.fetchone()

    if(data==None):
        return None
    
    user=User(data[0],data[1],data[2],data[3])
    return user   

    
    
