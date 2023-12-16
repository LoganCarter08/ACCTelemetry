"""
Assetto Corsa shared memory for Python applications

_ctypes.pyd must be somewhere in sys.path, because AC doesn't include all Python binaries.

Usage. Let's say you have following folder structure::

    some_app
        DLLs
            _ctypes.pyd
        some_app.py

some_app.py::

    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'DLLs'))

    from sim_info import info

    print(info.graphics.tyreCompound, info.physics.rpms, info.static.playerNick)


Do whatever you want with this code!
WBR, Rombik :)
"""
import mmap
import functools
import ctypes
from ctypes import c_int32, c_float, c_wchar

AC_STATUS = c_int32
AC_OFF = 0
AC_REPLAY = 1
AC_LIVE = 2
AC_PAUSE = 3
AC_SESSION_TYPE = c_int32
AC_UNKNOWN = -1
AC_PRACTICE = 0
AC_QUALIFY = 1
AC_RACE = 2
AC_HOTLAP = 3
AC_TIME_ATTACK = 4
AC_DRIFT = 5
AC_DRAG = 6
AC_FLAG_TYPE = c_int32

AC_NO_FLAG = 0
AC_BLUE_FLAG = 1
AC_YELLOW_FLAG = 2
AC_BLACK_FLAG = 3
AC_WHITE_FLAG = 4
AC_CHECKERED_FLAG = 5
AC_PENALTY_FLAG = 6

ACC_PENALTY_TYPE = c_int32 
ACC_None = 0 
ACC_DriveThrough_Cutting = 1 
ACC_StopAndGo_10_Cutting = 2 
ACC_StopAndGo_20_Cutting = 3 
ACC_StopAndGo_30_Cutting = 4
ACC_Disqualified_Cutting = 5
ACC_RemoveBestLaptime_Cutting = 6 
ACC_DriveThrough_PitSpeeding = 7
ACC_StopAndGo_10_PitSpeeding = 8
ACC_StopAndGo_20_PitSpeeding = 9
ACC_StopAndGo_30_PitSpeeding = 10
ACC_Disqualified_PitSpeeding = 11
ACC_RemoveBestLaptime_PitSpeeding = 12
ACC_Disqualified_IgnoredMandatoryPit = 13
ACC_PostRaceTime = 14
ACC_Disqualified_Trolling = 15
ACC_Disqualified_PitEntry = 16
ACC_Disqualified_PitExit = 17
ACC_Disqualified_Wrongway = 18
ACC_DriveThrough_IgnoredDriverStint = 19
ACC_Disqualified_IgnoredDriverStint = 20
ACC_Disqualified_ExceededDriverStintLimit = 21

ACC_TRACK_GRIP_STATUS = c_int32 
ACC_GREEN = 0 
ACC_FAST = 1 
ACC_OPTIMUM = 2
ACC_GREASY = 3 
ACC_DAMP = 4
ACC_WET = 5
ACC_FLOODED = 6 

ACC_RAIN_INTENSITY = c_int32 
ACC_NO_RAIN = 0 
ACC_DRIZZLE = 1 
ACC_LIGHT_RAIN = 2 
ACC_MEDIUM_RAIN = 3 
ACC_HEAVY_RAIN = 4 
ACC_THUNDERSTROM = 5

class SPageFilePhysics(ctypes.Structure):
    _pack_ = 4
    _fields_ = [
        ('packetId', c_int32),
        ('gas', c_float),
        ('brake', c_float),
        ('fuel', c_float),
        ('gear', c_int32),
        ('rpm', c_int32),
        ('steerAngle', c_float),
        ('speedKmh', c_float),
        ('velocity', c_float * 3),
        ('accG', c_float * 3),
        ('wheelSlip', c_float * 4),
        ('wheelLoadNOTUSED', c_float * 4),
        ('wheelPressure', c_float * 4),
        ('wheelAngularSpeed', c_float * 4),
        ('tyreWearNOTUSED', c_float * 4),
        ('tyreDirtyLevelNOTUSED', c_float * 4),
        ('tyreCoreTemperature', c_float * 4),
        ('camberRADNOTUSED', c_float * 4),
        ('suspensionTravel', c_float * 4),
        ('drsNOTUSED', c_float),
        ('tc', c_float),
        ('heading', c_float),
        ('pitch', c_float),
        ('roll', c_float),
        ('cgHeightNOTUSED', c_float),
        ('carDamage', c_float * 5),
        ('numberOfTyresOutNOTUSED', c_int32),
        ('pitLimiterOn', c_int32),
        ('abs', c_float),
        ('kersChargeNOTUSED', c_float),
        ('kersInputNOTUSED', c_float),
        ('autoShifterOn', c_int32),
        ('rideHeightNOTUSED', c_float * 2),
        ('turboBoost', c_float),
        ('ballastNOTUSED', c_float),
        ('airDensityNOTUSED', c_float),
        ('airTemp', c_float),
        ('roadTemp', c_float),
        ('localAngularVel', c_float * 3),
        ('finalFF', c_float),
        ('performanceMeterNOTUSED', c_float),
        ('engineBrakeNOTUSED', c_int32),
        ('ersRecoveryLevelNOTUSED', c_int32),
        ('ersPowerLevelNOTUSED', c_int32),
        ('ersHeatChargingNOTUSED', c_int32),
        ('ersIsChargingNOTUSED', c_int32),
        ('kersCurrentKJNOTUSED', c_float),
        ('drsAvailableNOTUSED', c_int32),
        ('drsEnabledNOTUSED', c_int32),
        ('brakeTemp', c_float * 4),
        ('clutch', c_float),
        ('tyreTempINOTUSED', c_float * 4),
        ('tyreTempMNOTUSED', c_float * 4),
        ('tyreTempONOTUSED', c_float * 4),
        ('isAIControlled', c_int32),
        ('tyreContactPoint', c_float * 4 * 3),
        ('tyreContactNormal', c_float * 4 * 3),
        ('tyreContactHeading', c_float * 4 * 3),
        ('brakeBias', c_float),
        ('localVelocity', c_float * 3),
        ('P2PActivationNOTUSED', c_int32), 
        ('P2PStatusNOTUSED', c_int32), 
        ('currentMaxRpmNOTUSED', c_float), 
        ('mzNOTUSED', c_float), 
        ('fxNOTUSED', c_float), 
        ('fyNOTUSED', c_float), 
        ('slipRation', c_float * 4), 
        ('slipAngle', c_float * 4), 
        ('tcinActionNOTUSED', c_int32), 
        ('absInActionNOTUSED', c_int32), 
        ('suspensionDamageNOTUSED', c_int32 * 4), 
        ('tyreTempNOTUSED', c_int32 * 4), 
        ('waterTemp', c_float), 
        ('brakePressure', c_float * 4), 
        ('frontBrakeCompund', c_int32), 
        ('rearBrakecompound', c_int32), 
        ('padLife', c_float * 4), 
        ('discLife', c_float * 4), 
        ('ignitionOn', c_int32), 
        ('starterEngineOn', c_int32), 
        ('isEngineRunning', c_int32), 
        ('kerbVibration', c_float), 
        ('slipVibrations', c_float), 
        ('gVibrations', c_float), 
        ('absVibrations', c_float)
    ]

class SPageFileGraphic(ctypes.Structure):
    _pack_ = 4
    _fields_ = [
        ('packetId', c_int32),
        ('status', AC_STATUS),
        ('session', AC_SESSION_TYPE),
        ('currentTime', c_wchar * 15),
        ('lastTime', c_wchar * 15),
        ('bestTime', c_wchar * 15),
        ('split', c_wchar * 15),
        ('completedLaps', c_int32),
        ('position', c_int32),
        ('iCurrentTime', c_int32),
        ('iLastTime', c_int32),
        ('iBestTime', c_int32),
        ('sessionTimeLeft', c_float),
        ('distanceTraveled', c_float),
        ('isInPit', c_int32),
        ('currentSectorIndex', c_int32),
        ('lastSectorTime', c_int32),
        ('numberOfLaps', c_int32),
        ('tyreCompound', c_wchar * 33),
        ('replayTimeMultiplier', c_float),
        ('normalizedCarPosition', c_float),
        ('activeCars', c_int32),
        ('carCoordinates', c_float * 3 * 60),
        ('carID', c_int32 * 60),
        ('playerCarId', c_int32),
        ('penaltyTime', c_float),
        ('flag', AC_FLAG_TYPE),
        ('penalty', ACC_PENALTY_TYPE),
        ('idealLineOn', c_int32),
        ('isInPitLine', c_int32),
        ('surfaceGrip', c_float),
        ('mandatoryPitDone', c_int32),
        ('windSpeed', c_float),
        ('windDirection', c_float),
        ('isSetupMenuVisible', c_int32), 
        ('mainDisplayIndex', c_int32), 
        ('secondaryDisplayIndex', c_int32), 
        ('TC', c_int32), 
        ('TCCUT', c_int32), 
        ('EngineMap', c_int32), 
        ('ABS', c_int32), 
        ('fuelXLap', c_float), 
        ('rainLights', c_int32), 
        ('flashingLights', c_int32), 
        ('lightsStage', c_int32), 
        ('exhaustTemperature', c_int32), 
        ('wiperLV', c_int32), 
        ('driverStintTotalTimeLeft', c_int32), 
        ('driverStintTimeLeft', c_int32), 
        ('rainTyres', c_int32), 
        ('sessionIndex', c_int32), 
        ('usedFuel', c_float), 
        ('deltaLapTime', c_wchar * 15),
        ('iDeltaLapTime', c_int32), 
        ('estimatedLapTime', c_wchar * 15), 
        ('iEstimatedLapTime', c_int32), 
        ('isDeltaPositive', c_int32), 
        ('iSplit', c_int32), 
        ('isValidLap', c_int32), 
        ('fuelEstimatedLaps', c_float), 
        ('trackStatus', c_wchar * 33), 
        ('missingMandatoryPits', c_int32), 
        ('clock', c_int32), 
        ('directionLightsLeft', c_int32), 
        ('directionLightsRight', c_int32), 
        ('globalYellow', c_int32), 
        ('globalYellow1', c_int32), 
        ('globalYellow2', c_int32), 
        ('globalYellow3', c_int32), 
        ('globalWhite', c_int32), 
        ('globalGreen', c_int32), 
        ('globalCheckered', c_int32), 
        ('globalRed', c_int32), 
        ('mfdTyreSet', c_int32), 
        ('mfdFuelToAdd', c_float), 
        ('mfdTyrePressureLF', c_float), 
        ('mfdTyrePressureRF', c_float), 
        ('mfdTyrePressureLR', c_float), 
        ('mfdTyrePressureRR', c_float), 
        ('trackGripStatus', ACC_TRACK_GRIP_STATUS), 
        ('rainIntensity', ACC_RAIN_INTENSITY), 
        ('rainIntensityIn10Min', ACC_RAIN_INTENSITY), 
        ('rainIntensityIn30Min', ACC_RAIN_INTENSITY), 
        ('currentTyreSet', c_int32), 
        ('strategyTyreSet', c_int32), 
        ('gapAhead', c_int32), 
        ('gapBehind', c_int32)
    ]

class SPageFileStatic(ctypes.Structure):
    _pack_ = 4
    _fields_ = [
        ('_smVersion', c_wchar * 15),
        ('_acVersion', c_wchar * 15),
        ('numberOfSessions', c_int32),
        ('numCars', c_int32),
        ('carModel', c_wchar * 33),
        ('track', c_wchar * 33),
        ('playerName', c_wchar * 33),
        ('playerSurname', c_wchar * 33),
        ('playerNick', c_wchar * 33),
        ('sectorCount', c_int32),
        ('maxTorqueNOTUSED', c_float),
        ('maxPowerNOTUSED', c_float),
        ('maxRpm', c_int32),
        ('maxFuel', c_float),
        ('suspensionMaxTravelNOTUSED', c_float * 4),
        ('tyreRadiusNOTUSED', c_float * 4),
        ('maxTurboBoostNOTUSED', c_float),
        ('depreciated_1NOTUSED', c_float),
        ('depreciated_2NOTUSED', c_float),        
        ('penaltiesEnabled', c_int32),
        ('aidFuelRate', c_float),
        ('aidTireRate', c_float),
        ('aidMechanicalDamage', c_float),
        ('aidAllowTyreBlankets', c_int32),
        ('aidStability', c_float),
        ('aidAutoClutch', c_int32),
        ('aidAutoBlip', c_int32),
        ('hasDRSNOTUSED', c_int32),
        ('hasERSNOTUSED', c_int32),
        ('hasKERSNOTUSED', c_int32),
        ('kersMaxJNOTUSED', c_float),
        ('engineBrakeSettingsCountNOTUSED', c_int32),
        ('ersPowerControllerCountNOTUSED', c_int32),
        ('trackSplineLengthNOTUSED', c_float),
        ('trackConfigurationNOTUSED', c_wchar * 33),
        ('ersMaxJNOTUSED', c_float),
        ('isTimedRaceNOTUSED', c_int32),
        ('hasExtraLapNOTUSED', c_int32),
        ('carSkinNOTUSED', c_wchar * 33),
        ('reversedGridPositionsNOTUSED', c_int32),
        ('pitWindowStart', c_int32),
        ('pitWindowEnd', c_int32),
        ('isOnline', c_int32), 
        ('dryTyresName', c_wchar * 33), 
        ('wetTyresName', c_wchar * 33)
    ]

class SimInfo:
    def __init__(self):
        self._acpmf_physics = mmap.mmap(0, ctypes.sizeof(SPageFilePhysics), "acpmf_physics")
        self._acpmf_graphics = mmap.mmap(0, ctypes.sizeof(SPageFileGraphic), "acpmf_graphics")
        self._acpmf_static = mmap.mmap(0, ctypes.sizeof(SPageFileStatic), "acpmf_static")
        self.physics = SPageFilePhysics.from_buffer(self._acpmf_physics)
        self.graphics = SPageFileGraphic.from_buffer(self._acpmf_graphics)
        self.static = SPageFileStatic.from_buffer(self._acpmf_static)

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

def do_test():
    for struct in info.static, info.graphics, info.physics:
        print(struct.__class__.__name__)
        for field, type_spec in struct._fields_:
            value = getattr(struct, field)
            if not isinstance(value, (str, float, int)):
                value = list(value)
            print(" {} -> {} {}".format(field, type(value), value))

if __name__ == '__main__':
    #do_test()
    demo()