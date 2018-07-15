#User Module


class User:
    def __init__(self,userid,name,password,type):
        self.userid=userid
        self.name=name
        self.password=password
        self.type=type

    def SetUserId(self,userid):
        self.userid=userid

    def SetName(self,name):        
        self.name=name

    def SetPassword(self,password):
        self.password=password

    def SetType(self,type):
        self.type=type


    def GetUserId(self):
        return self.userid

    def GetName(self):
        return self.name

    def GetPassword(self):
        return self.password

    def GetType(self):
        return self.type
