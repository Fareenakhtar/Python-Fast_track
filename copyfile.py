import sys
input1 = sys.argv[1]

with open('C:\FAST_TRACT_COURSE\Fareen_201046038_Sample_3\Fareen_201046038_Sample_3_soln\output.txt', 'a') as f1,open('C:\FAST_TRACT_COURSE\Fareen_201046038_Sample_3\Fareen_201046038_Sample_3_soln\input.txt','r') as f:
    for line in f:
        f1.write(line)




