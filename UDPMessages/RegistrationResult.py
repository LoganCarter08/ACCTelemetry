import struct 
class RegistrationResult: 
    def __init__(self, aPacket): 
        self.connectionId = None 
        self.connectionSuccess = None 
        self.isReadOnly = None 
        self.errorMessage = None 
        errorMessageLen = -1

        # used for the initial state 
        if aPacket == None: 
            return 

        self.parsePacket(aPacket)

    def parsePacket(self, aPacket):
        try: 
            # the following shows two ways to get data out of the byte array. 
            # the int.from_bytes only works for ints, but the data passed to us isn't
            # conventional boolean behavior according to the example program, so we'll 
            # read it as a single bit int and treat them the way the example code does. 
            self.connectionId = struct.unpack('i', aPacket[1:5])[0]
            self.connectionSuccess = int.from_bytes(aPacket[5:6], "little") > 0
            self.isReadOnly = int.from_bytes(aPacket[6:7], "little") == 0
            errorMessageLen = struct.unpack('H', aPacket[7:9])[0]
            # errorMessage behavior untested!! Assumptions were made 
            self.errorMessage = aPacket[9:9 + errorMessageLen].decode()
        except Exception as e: 
            print("Caught the following exception parsing Registration Result: ", str(e))