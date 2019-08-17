import sys
import os
import subprocess
from live_rep2 import start

# Name of the folder that contains the videos
VIDEO_FOLDER = "blade" if len(sys.argv) < 2 else sys.argv[1]

# Count for all videos in that folder
ACTUAL_COUNT = 5


vids = os.listdir(VIDEO_FOLDER)
not_in = [".divxconverter.temp", ".DS_Store", "annotations"]
vids = list(filter(lambda x: x not in not_in, vids))

print "Total videos found in %s = "%VIDEO_FOLDER, len(vids)

i=1

absolute_errors_per_video = []
total_error = 0.0
for item in vids:
    count = int(start("%s/%s"%(VIDEO_FOLDER, item)))
    difference = abs(count - ACTUAL_COUNT)
    absolute_errors_per_video.append(difference)
    total_error = total_error + difference
    print "ERRORS PER VIDEO = ", absolute_errors_per_video
    print "TOTAL ERROR SO FAR = ", total_error
    i = i+1

mae = total_error/len(vids)
print "MEAN ABSOLUTE ERROR ON %s = "%VIDEO_FOLDER, mae
