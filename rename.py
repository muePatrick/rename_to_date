import os
import exifread  # pip install exifread
from datetime import datetime
import sys

HEADER = '\033[95m'  # purple
OKBLUE = '\033[94m'  # blue
OKGREEN = '\033[92m'  # green
WARNING = '\033[93m'  # yellow
FAIL = '\033[91m'  # red
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

if (len(sys.argv) != 2):
    print("Please give a directory path")
    exit(-2)
    
if not (os.path.isdir(sys.argv[1])):
    print("Directory path seems wrong")
    exit(-2)
    
if not (os.path.exists(sys.argv[1])):
    print("Directory path does not exist")
    exit(-2)


if __name__ == "__main__":
    print("\n" + HEADER + "############################")
    print("# Sorting Pictures By Date #")
    print("############################" + ENDC)
    
    path = str(sys.argv[1]) + "/"
    print("\n" + OKBLUE + UNDERLINE + "Working in " + path + ENDC + "\n")

    for filename in os.listdir(path):
        
        filename = filename.lower()
        if not (filename.endswith(".jpg")):
            continue

        x = os.stat(path + filename)
        f = open(path + filename, "rb")
        y = exifread.process_file(f)
        f.close()

        ht = []

        ht.append(datetime.fromtimestamp(x.st_atime))
        ht.append(datetime.fromtimestamp(x.st_ctime))
        ht.append(datetime.fromtimestamp(x.st_mtime))
        
        ht.append(datetime.strptime(str(y["EXIF DateTimeOriginal"]), '%Y:%m:%d %H:%M:%S'))
        ht.append(datetime.strptime(str(y["Image DateTime"]), '%Y:%m:%d %H:%M:%S'))
        
        mt = min(ht)
        
        os.rename(path + filename, path + str(mt).replace(":", ".") + " " + str(x.st_size/1000000) + "MB.jpg" )
        
        print(OKGREEN + "Current file: " + BOLD + filename + ENDC + OKGREEN + " -> Oldest date: " + WARNING + str(mt) + ENDC)
        
    print("\n")
    print(FAIL + "All done!" + ENDC)
    print("\n")