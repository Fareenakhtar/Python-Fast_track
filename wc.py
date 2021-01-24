import sys

word=0
l=0
with open('C:\FAST_TRACT_COURSE\Fareen_201046038_Sample_3\Fareen_201046038_Sample_3_soln\cat.txt','r') as file:
    for line in file:
        l+=1
        word+=len(line.split(','))

file=open('C:\FAST_TRACT_COURSE\Fareen_201046038_Sample_3\Fareen_201046038_Sample_3_soln\cat.txt','r')
data=file.read()
char=len(data)
print("Total charectors are: ",char)
print("Total words are: ",word)
print("Total lines are: ",l)
