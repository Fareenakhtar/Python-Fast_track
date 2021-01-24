import os

import re
print("Enter file name: ")
file=input()

print("Enter a pattern:")
word=input()
print("")

word=word+'.+'

fopen=open(file,'r')
for row in fopen:
    if re.search(word,row):
        print(row)
        
    
    
