import os

#folder path input 
print("Enter folder path") 
path = os.path.abspath(input()) 


print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
