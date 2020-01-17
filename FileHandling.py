
import os
os.chdir(r'C:\Users\vkumar15\Desktop') #cd dir 

f = open('Chapter-03.txt') #default mode is r
#print(f.read())
#print(f.readline())
#print(f.readline())
#print(f.readline())
o = f.readlines()

f.close()

print(o)
print(type(o))

for r in o:
    print(r)

#row count
print(len(o))





