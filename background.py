import os
import shutil

source = input("Enter source folder name ")
destination = input("Enter destination folder name ")
source = source + '/'
destination = destination + '/'
print(source)
print(destination)
list = os.listdir(source)
for file in list:
    shutil.copy((source+file),destination)
