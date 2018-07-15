#Flight Module

class Flight:
    def __init__(self,flightno,name,source,destination,fare,availability):
        self.flightno=flightno
        self.name=name
        self.source=source
        self.destination=destination
        self.fare=fare
        self.availability=availability

    def SetFlightNo(self,flightno):
        self.flightno=flightno

    def SetName(self,name):
        self.name=name

    def SetSource(self,source):
        self.source=source

    def SetDestination(self,destination):
        self.destination=destination

    def SetFare(self,fare):
        self.fare=fare

    def GetAvailability(self):
        return self.availability

    def GetFlightNo(self):
        return self.flightno

    def GetName(self):
        return self.name

    def GetSource(self):
        return self.source

    def GetDestination(self):
        return self.destination

    def GetFare(self):
        return self.fare

    def SetAvailability(self,availability):
        self.availability=availability
    
