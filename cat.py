import sys

print ('Number of arguments ', len(sys.argv),' arguments.')
print ('Argument List:', str(sys.argv))
f=sys.argv[1]
fopen= open(f,'r')

for row in fopen:
    print(row)
