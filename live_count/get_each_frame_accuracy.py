import sys
import os
import subprocess
import numpy as np
from live_rep_refactor import start

# Name of the folder that contains the videos
VIDEO_FOLDER = "blade" if len(sys.argv) < 2 else sys.argv[1]

ANNOTATIONS = "annotations"
# Count for all videos in that folder
ACTUAL_COUNT = 5


vids = os.listdir(VIDEO_FOLDER)
not_in = [".divxconverter.temp", ".DS_Store", "annotations"]
vids = list(filter(lambda x: x not in not_in, vids))  

print "Total videos found in %s = "%VIDEO_FOLDER, len(vids)

from scipy.signal import resample

i=1
accuracy_per_video = []
for item in vids:
    preds_per_frame = start("%s/%s"%(VIDEO_FOLDER, item))
    actual_labels_per_frame = np.load(os.path.join(VIDEO_FOLDER, ANNOTATIONS, item[:item.rfind(".")]+".npy")).tolist()
    # no such thing as 1 repetition
    actual_labels_per_frame = list(map(lambda x: x+1 if x>0 else x, actual_labels_per_frame))
    
    preds_per_frame = resample(preds_per_frame, len(actual_labels_per_frame))
    preds_per_frame = list(map(lambda x: int(round(x)),preds_per_frame))
    print("PRED:", len(preds_per_frame), preds_per_frame)
    print("ACTUAL:", len(actual_labels_per_frame), actual_labels_per_frame)
    correct = 0
    for it, frame in enumerate(preds_per_frame):
        if frame == actual_labels_per_frame[it]:
            correct += 1
    accuracy = (float(correct)/float(len(preds_per_frame)))*100.00
    accuracy_per_video.append(accuracy)
    print "ACCURACY PER VIDEO = ", accuracy_per_video
    i = i+1

ta = sum(accuracy_per_video)/len(accuracy_per_video)
print "TOTAL EACH FRAME ACCURACY ON %s = "%VIDEO_FOLDER, ta
