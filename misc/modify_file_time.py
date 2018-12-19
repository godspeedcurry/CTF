from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle 
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import time
import sys
import os

if len(sys.argv)<5:
  pfile = os.path.basename(sys.argv[0])
  print("USAGE:\n\t%s <createTime> <modifyTime> <accessTime> <FileName>\n" % pfile)
  print("EXAMPLE:")
  print('%s "01.01.2000 00:00:00" "01.01.2000 00:00:00" "01.01.2000 00:00:00" file' % (pfile))
  # sys.exit()  

# get arguments  
cTime = sys.argv[1] # create
mTime = sys.argv[2] # modify
aTime = sys.argv[3] # access
fName = sys.argv[4]

# get arguments  
# cTime = "01.01.2001 00:00:00"
# mTime = "01.01.2001 00:00:00"
# aTime = "01.01.2001 00:00:00"
# fName = "1.png"

# specify time format
format = "%d.%m.%Y %H:%M:%S"
offset = 0 # in seconds

# create struct_time object
cTime_t = time.localtime(time.mktime(time.strptime(cTime,format))+offset)
mTime_t = time.localtime(time.mktime(time.strptime(mTime,format))+offset)
aTime_t = time.localtime(time.mktime(time.strptime(aTime,format))+offset)

# visually check if conversion was ok
print()
print("FileName: %s" % fName)
print("Create  : %s --> %s OK" % (cTime,time.strftime(format,cTime_t)))
print("Modify  : %s --> %s OK" % (mTime,time.strftime(format,mTime_t)))
print("Access  : %s --> %s OK" % (aTime,time.strftime(format,aTime_t)))
print()

# change timestamp of file
fh = CreateFile(fName, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0) 
createTime, accessTime, modifyTime = GetFileTime(fh) 
print("Change Create from",createTime,"to %s" % (time.strftime(format,cTime_t)))
print("Change Modify from",modifyTime,"to %s" % (time.strftime(format,mTime_t)))
print("Change Access from",accessTime,"to %s" % (time.strftime(format,aTime_t)))
print()

createTime = Time(time.mktime(cTime_t))
accessTime   = Time(time.mktime(aTime_t))
modifyTime    = Time(time.mktime(mTime_t))
SetFileTime(fh, createTime, accessTime, modifyTime) 
CloseHandle(fh)

# check if all was ok
ctime = time.strftime(format,time.localtime(os.path.getctime(fName)))
mtime = time.strftime(format,time.localtime(os.path.getmtime(fName)))
atime = time.strftime(format,time.localtime(os.path.getatime(fName)))

print("CHECK MODIFICATION:")
print("FileName: %s" % fName)
print("Create  : %s" % (ctime))
print("Modify  : %s" % (mtime))
print("Access  : %s" % (atime))

# from zhihu
