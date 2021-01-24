import os
import sys

Folder_path=r'f1'
f1=sys.argv[1]

def listDir(dir):
    fileNames=os.listdir(dir)
    max_mtime=0
    for fileName in fileNames:
        full_path = os.path.join(dir, fileName)
        mtime = os.stat(full_path).st_mtime
        if mtime > max_mtime:
            max_mtime = mtime
            max_dir = dir
            max_file = fileName
    print(max_dir, max_file)
    


if __name__ == '__main__' or __name__ != '__main__':
    listDir(f1)

