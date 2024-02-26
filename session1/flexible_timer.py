import time
import sys

time2sleep = sys.argv[1]

for i in range(int(time2sleep)):
    print(f"{i+1}")
    time.sleep(1)