import struct 
class RealtimeUpdate: 
    def __init__(self, aPacket): 
        self.eventIndex = None 
        self.sessionIndex = None 
        self.sessionType = None 
        self.phase = None 
        self.sessionTime = None 
        self.sessionEndTime = None 
        self.focusedCarIndex = None 
        self.activeCameraSet = None 
        self.activeCamera = None 
        self.currentHudPage = None 
        self.isReplayPlaying = None 
        self.replaySessionTime = None 
        self.replayRemainingTime = None
        self.timeOfDay = None 
        self.ambientTemp = None 
        self.trackTemp = None 
        self.clouds = None 
        self.rainLevel = None 
        self.wetness = None 
        self.bestSessionLap = None 

        # used for the initial state 
        if aPacket == None: 
            return 

        self.parsePacket(aPacket)

    def parsePacket(self, aPacket):
        try: 
            self.eventIndex = struct.unpack('H', aPacket[1:3])[0]
            self.sessionIndex = struct.unpack('H', aPacket[3:5])[0]
            self.sessionType = int.from_bytes(aPacket[5:6], "little")
            self.phase = int.from_bytes(aPacket[6:7], "little")
            self.sessionTime = struct.unpack('f', aPacket[7:11])[0]
            self.sessionEndTime = struct.unpack('f', aPacket[11:15])[0]
            self.focusedCarIndex = struct.unpack('i', aPacket[15:19])[0]

            activeCameraSetLength = struct.unpack('H', aPacket[19:21])[0]
            self.activeCameraSet = aPacket[21:21 + activeCameraSetLength].decode()
            lastByte = 21 + activeCameraSetLength

            activeCameraLength = struct.unpack('H', aPacket[lastByte:lastByte + 2])[0]
            lastByte += 2
            self.activeCamera = aPacket[lastByte:lastByte + activeCameraLength].decode()
            lastByte += activeCameraLength

            currentHudPageLength = struct.unpack('H', aPacket[lastByte:lastByte + 2])[0]
            lastByte += 2
            self.currentHudPage = aPacket[lastByte:lastByte + currentHudPageLength].decode()
            lastByte += currentHudPageLength 

            self.isReplayPlaying = struct.unpack('?', aPacket[lastByte:lastByte + 1])[0]
            lastByte += 1

            if self.isReplayPlaying: 
                self.replaySessionTime = struct.unpack('f', aPacket[lastByte:lastByte + 4])[0]
                lastByte += 4
                self.replayRemainingTime = struct.unpack('f', aPacket[lastByte:lastByte + 4])[0]
                lastByte += 4
            
            self.timeOfDay = self.replayRemainingTime = struct.unpack('f', aPacket[lastByte:lastByte + 4])[0]
            lastByte += 4

            self.ambientTemp = int.from_bytes(aPacket[lastByte:lastByte + 1], "little", signed=False)
            lastByte += 1 

            self.trackTemp = int.from_bytes(aPacket[lastByte:lastByte + 1], "little", signed=False)
            lastByte += 1 

            self.clouds = int.from_bytes(aPacket[lastByte:lastByte + 1], "little", signed=False) / 10.0
            lastByte += 1 

            self.rainLevel = int.from_bytes(aPacket[lastByte:lastByte + 1], "little", signed=False) / 10.0
            lastByte += 1 

            self.wetness = int.from_bytes(aPacket[lastByte:lastByte + 1], "little", signed=False) / 10.0
            lastByte += 1 

            print("Add lap parsing here later")
        except Exception as e: 
            print("Caught the following exception parsing Realtime Update: ", str(e))