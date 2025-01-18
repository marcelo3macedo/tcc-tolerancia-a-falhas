import time, os
from datetime import datetime
from lib.schedule import getScheduleInfos
from lib.requester import sendRequests

def run(scheduleFile, processType):    
    while True:
        [messageCount] = getScheduleInfos(scheduleFile)

        print(f"Sending {messageCount} /message requests")
        
        endpoint = '/message/cpu' if processType == 'cpu' else '/message/memory'
        sendRequests(endpoint, messageCount)
        
        time.sleep(60 - datetime.now().second)

if __name__ == "__main__":
    process_type = os.getenv("TYPE", "cpu")
    schedule_file = "config/requestSchedule.json"
    run(schedule_file, process_type)
