"""
This code started out from an AC parser, but was extended for ACC. I can't
find the original devs/repo, but their names were:  WBR, Rombik. 
Much credit goes to them as it made writing this much quicker. 
"""
import mmap
import functools
import ctypes
from ctypes import c_int32, c_float, c_wchar
import sys

from SharedMemory import SPageFileGraphics, SPageFilePhysics, SPageFileStatic

class SimInfo:
    def __init__(self):
        self._acpmf_physics = mmap.mmap(0, ctypes.sizeof(SPageFilePhysics.SPageFilePhysics), "acpmf_physics")
        self._acpmf_graphics = mmap.mmap(0, ctypes.sizeof(SPageFileGraphics.SPageFileGraphics), "acpmf_graphics")
        self._acpmf_static = mmap.mmap(0, ctypes.sizeof(SPageFileStatic.SPageFileStatic), "acpmf_static")
        self.physics = SPageFilePhysics.SPageFilePhysics.from_buffer(self._acpmf_physics)
        self.graphics = SPageFileGraphics.SPageFileGraphics.from_buffer(self._acpmf_graphics)
        self.static = SPageFileStatic.SPageFileStatic.from_buffer(self._acpmf_static)

    def close(self):
        try: 
            self._acpmf_physics.close()
            self._acpmf_graphics.close()
            self._acpmf_static.close()
        except:
            pass

    def __del__(self):
        self.close()

info = SimInfo()

def demo():
    import time

    for _ in range(400):
        print(info.static.track, info.graphics.tyreCompound, info.graphics.currentTime,
              info.physics.rpm, info.graphics.currentTime, info.static.maxRpm)
        time.sleep(0.1)
        sys.stdout.flush()

def do_test():
    for struct in info.static, info.graphics, info.physics:
        print(struct.__class__.__name__)
        for field, type_spec in struct._fields_:
            value = getattr(struct, field)
            if not isinstance(value, (str, float, int)):
                value = list(value)
            print(" {} -> {} {}".format(field, type(value), value))
            sys.stdout.flush()

if __name__ == '__main__':
    #do_test()
    demo()