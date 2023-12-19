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

class SPageFileGraphics(ctypes.Structure):
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