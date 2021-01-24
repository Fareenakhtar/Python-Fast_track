import sys
f='C:\FAST_TRACT_COURSE\Fareen_201046038_Sample_3\Fareen_201046038_Sample_3_soln\sumfile.txt'
print(f)
fopen=open(f,"r")
fr=fopen.read()
tot=0
for line in fr:
    for num in line.split():
        tot=tot+float(num.strip())

print("The sum of the number is:",tot)
    
