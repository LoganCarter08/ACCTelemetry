import struct 
import binascii
import socket
import sys
import io

try: 
    from .RegistrationResult import RegistrationResult 
    from .RealtimeUpdate import RealtimeUpdate
except: 
    from RegistrationResult import RegistrationResult 
    from RealtimeUpdate import RealtimeUpdate

class ACCUDP():
    def __init__(self, aIP, aPort, aDisplayName, aConnectionPassword, aCommandPassword = ""):
        self.displayName = aDisplayName
        self.connectionPassword = aConnectionPassword
        self.commandPassword = aCommandPassword 
        self.ip = aIP 
        self.port = aPort 

        # every time we get a new message of the following types these fields will 
        # be updated so the user can have quick and easy access 
        self.registrationResult = RegistrationResult(None)
        self.realTimeUpdate = RealtimeUpdate(None)
        self.realTimeCarUpdate = None 
        self.entryList = None 
        self.trackData = None 
        self.entryListCar = None 

        self.setupConnection()
    
    def createRegistrationMessage(self): 
        outVar = struct.pack('BBH', 1, 4, len(self.displayName))
        outVar = outVar + bytearray(self.displayName, 'utf-8')
        outVar = outVar + struct.pack('H', len(self.connectionPassword))
        outVar = outVar + bytearray(self.connectionPassword, 'utf-8')
        outVar = outVar + struct.pack('IH', 250, len(self.commandPassword)) 
        outVar = outVar + bytearray(self.commandPassword, 'utf-8')
        # probably redundant to call with bytes, but 
        # redundancy never hurt anybody. 
        return bytes(outVar) 

    def setupConnection(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # we'll leave this as 9001 for now because the 
        # user probably doesn't care what ip they use. 
        # 9001 doesn't seem to be a commonly used port. 
        self.sock.bind(("127.0.0.1", 9001))
        self.sock.setblocking(False)
        self.sock.settimeout(.05)

        self.tryToConnect() 

    def tryToConnect(self):
        # by the time we are here we should be ready to communicate with ACC
        # However what if we are running before the UDP connection is ready? 
        # We need to send registration until we get a valid response/don't timeout. 
        while not self.registrationResult.connectionSuccess: 
            try: 
                data = self.sock.recvfrom(4096)
                self.handleResponse(data)
            except: 
                self.sendRegistration()

    def getNewData(self):
        # now that we are connected we can start handling more message types 
        try: 
            data = self.sock.recvfrom(4096)
            self.handleResponse(data)
        except: 
            pass 
        
        # python likes to get clogged up with sockets being involved. 
        # flush her out. 
        sys.stdout.flush()
    
    def handleResponse(self, aData):
        self.connected = True 
        data = aData[0]
        match int.from_bytes(data[0:1], "little"):
            case 1:
                self.registrationResult.parsePacket(data)
            case 2:
                print("Realtime Update")
                self.realTimeUpdate.parsePacket(data)
            case 3: 
                print("Realtime Car Update")
            case 4: 
                print("Entry List")
            case 5: 
                print("Track Data")
            case 6: 
                print("Entry List Car")
            case 7: 
                print("Broadcast Event") 
    
    def sendRegistration(self):
        self.sock.sendto(self.createRegistrationMessage(), (self.ip, self.port))

if __name__ == '__main__':
    accudp = ACCUDP("localhost", 9000, "testing", "asd")
    while True: 
        accudp.getNewData()