import os,time
import datetime
import shutil

import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
print(ago)
strftime = "%H:%M %m/%d/%Y"
source= "/Users/mhtab/OneDrive/Desktop/Origin Folder/"
dest = "/Users/mhtab/OneDrive/Desktop/Destination/"

for root, dirs,files in os.walk(source):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)
        print(st)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        print(mtime)
        if mtime > ago:
            print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.move(path, dest)
