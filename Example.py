from SharedMemory import ACCSharedMemory
from UDPMessages import ACCUDP 

if __name__ == '__main__':
    accudp = ACCUDP.ACCUDP("localhost", 9000, "testing", "asd")
    accSharedMemory = ACCSharedMemory.ACCSharedMemory()
    while True: 
        accudp.getNewData()
        # Here add some examples about extracting data. 
        # May need to add a new request for data at some point. 

        # print some data out of the shared memory
        print(accSharedMemory.static.track, accSharedMemory.graphics.tyreCompound, accSharedMemory.graphics.currentTime,
              accSharedMemory.physics.rpm, accSharedMemory.graphics.currentTime, accSharedMemory.static.maxRpm)
