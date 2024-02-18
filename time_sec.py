' code to run current time in seconds ' 

import time
import math
while True:
    current_time = time.localtime()
    hours= current_time.tm_hour
    min= current_time.tm_min
    sec= current_time.tm_sec
    TIme_in_sec = hours * 3600 + min * 60 + sec
    
    print("TIme_in_se:", TIme_in_sec)
    time.sleep(1)