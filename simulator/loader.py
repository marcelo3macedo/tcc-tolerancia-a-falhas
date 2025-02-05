import time, os
from datetime import datetime
from lib.schedule import getScheduleInfos
from lib.requester import sendRequests

def run(scheduleFile, processType):
    time.sleep(60)
    options = getScheduleInfos(scheduleFile)

    for o in options:
        print(f"Sending {o} /message requests")
        
        endpoint = '/message/cpu' if processType == 'cpu' else '/message/memory'
        
        sendRequests(endpoint, o)
        
        time.sleep(60 - datetime.now().second)
    
    while True:
        time.sleep(600)

if __name__ == "__main__":
    process_type = os.getenv("TYPE", "cpu")
    schedule_file = "config/requestSchedule.json"
    run(schedule_file, process_type)
