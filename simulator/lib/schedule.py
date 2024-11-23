from datetime import datetime
from lib.json import loadFileFromJson

def getScheduleInfos(scheduleFile):
    schedule = loadFileFromJson(scheduleFile)

    currentTime = datetime.now().strftime("%M")
    lastDigit = currentTime[-1]

    if not lastDigit in schedule:
        print(f"Time: {lastDigit} | No requests scheduled.")
        return

    messageCount = schedule[lastDigit].get("message", 0)
    statusCount = schedule[lastDigit].get("message_status", 0)

    return {
        messageCount,
        statusCount
    }
