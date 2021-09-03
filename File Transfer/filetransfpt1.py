import shutil
import os

#set where the source of the files are
source = "/Users/mhtab/OneDrive/Desktop/Origin Folder/"
print(source)

#set the destination path to folderB
destination = "/Users/mhtab/OneDrive/Desktop/destination/"
print(destination)
files = os.listdir(source)

for i in files:
    print(i)
    #we are saying move the files represented by i' to their new destination
    shutil.move(source+i, destination)
    print(source+i)
