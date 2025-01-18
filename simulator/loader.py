import time
from datetime import datetime
from lib.schedule import getScheduleInfos
from lib.requester import sendRequests

def run(scheduleFile):    
    while True:
        [messageCount, statusCount] = getScheduleInfos(scheduleFile)

        print(f"Sending {messageCount} /message requests and {statusCount} /message/status requests")
        
        sendRequests("/message/memory", messageCount)
        
        time.sleep(60 - datetime.now().second)

if __name__ == "__main__":
    schedule_file = "config/requestSchedule.json"
    run(schedule_file)
