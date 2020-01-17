import os
os.chdir(r'C:\Users\vkumar15\Desktop') #cd dir 

f = open('out.txt','a') #default mode is r

#f.write('hi\n')
#f.write('hello\n')

for i in range(5): #0 to 4
    d = input('enter data :')
    f.write(d+'\n')
    
f.close()

