from zipfile import ZipFile
import rarfile
import os

path = "C:/Users/dusta/Downloads"
extraction_path = "C:/Users/dusta/OneDrive/Documents/EA Games/The Sims 2/Downloads"

dir_list = os.listdir(path)

for x in dir_list:
    if x.endswith(".zip"):
        with ZipFile(path+"/"+x, 'r') as zipObj:
            zipObj.extractall(extraction_path)
            print("\n" + x + " extracted")
    elif x.endswith(".rar"):
       rarfile.RarFile(path+"/"+x).extractall(extraction_path)
       print("\n" + x + " extracted")

print(os.listdir(extraction_path).__len__)


