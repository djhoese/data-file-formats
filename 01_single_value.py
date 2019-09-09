import os
import sys
from datetime import datetime, timedelta

FILENAME = 'last_time.txt'

def main():
    mode = 'r+' if os.path.isfile(FILENAME) else 'w+'
    now = datetime.utcnow()
    with open(FILENAME, mode) as time_file:
        last_time = time_file.read().strip()
        if last_time:
            last_dt = datetime.fromtimestamp(float(last_time))
            diff = int((now - last_dt).total_seconds())
            print("This script was run {:d} seconds ago.".format(diff))
        else:
            diff = None
            print("This is the first time this script has been run.")

        # write the current time
        time_file.seek(0)  # go back to the start of the file
        time_file.write("{:f}\n".format(now.timestamp()))

if __name__ == "__main__":
    sys.exit(main())
