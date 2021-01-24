import os

path='C:\PYTHON\Fareen_201046038_Sample_3'
print("Enter folder path:")
path=os.path.abspath(input())

a=[ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ]
print(a)
