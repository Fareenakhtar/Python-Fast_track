import os
import re
print("Enter folder path:")
path=os.path.abspath(input())

print("Enter the wildcard pattern: ")
word=input()
word=word+'.+'
print("")
print("")

a=[]
a=[ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ]

for i in a:
    if re.search(word,i):
        print(i)
