from pytube import YouTube

import os
import shutil
import math
import datetime
import pickle
import sys

import matplotlib.pyplot as plt

import cv2

url = input("Video URL: ")
video = YouTube(f"{url}")

count = 0
vids = video.streams.filter(progressive=True, file_extension="mp4")
for vid in vids:
    count += 1
    print(f"\n{count}:\n {vid}\n\n")
    
res_choice = f"{count + 1}"
try:
    while(int(res_choice) > count):
        res_choice = input(f"Enter stream number (1 to {count})")
    video = vids[int(res_choice) - 1]
except ValueError:
    print("ERROR - cannot convert to int")
    sys.exit()


cwd = os.getcwd()
file_name = "downloadpath.txt"
if not os.path.exists(f"{cwd}\{file_name}"):
    downloadpath = input("Enter the exact path of the folder you would like to download this videos and all future videos into: ")
    with open(file_name, "w") as f:
        f.write(downloadpath)
else:
    with open(file_name, "r") as f:
        downloadpath = f.read()

video.download(downloadpath)
print(f"Video succesfully saved in {downloadpath}")









