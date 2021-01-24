import sys
print ('Number of arguments ', len(sys.argv),' arguments.')
print ('Argument List:', str(sys.argv))
f=sys.argv[1]
print(f)
fopen=open(f,"r")
for i in range(0,5):
    print(fopen.readline())
