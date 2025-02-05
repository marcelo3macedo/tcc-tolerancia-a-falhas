from lib.json import loadFileFromJson

def getScheduleInfos(scheduleFile):
    return loadFileFromJson(scheduleFile)
