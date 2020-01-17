import os
os.chdir(r'C:\Users\vkumar15\Desktop') #cd dir 

def create_file(name,data):
    f = open(name,'w')
    f.write(data+"\n")
    f.close()
    print('file is saved')
    
    


def read_file(add):
    a = open(add,'r')
    print(a.read())
    a.close()
    
    
    
