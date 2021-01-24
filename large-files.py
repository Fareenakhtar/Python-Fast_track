import os

print("Enter folder path:")
path=os.path.abspath(input())

print("Enter the size: ")
max_size=input()

print("Enter 'M' if the size is in MB,'G' if the size is in GB, 'K' if the size is in KB")
n_byte=input()


max_file=""

for folder,subfolders,files in os.walk(path):
    for file in files:
        size=os.stat(os.path.join(folder,file)).st_size
        if n_byte=='M':
            if size>(int(max_size)*int(1048576)):
                print(file)
                print('Size: '+str(size))
        elif n_byte == 'G':
            if size>(int(max_size)*int(1000*1048576)):
                print(file)
                print('Size: '+str(size))
        else:
            if size>(int(max_size)*int(1000*1048576)):
                print(file)
                print('Size: '+str(size))



            
                                       


