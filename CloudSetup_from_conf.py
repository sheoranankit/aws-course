#cloud setup

from CreateS3Bucket_2 import *

f = open(r'C:\Users\vkumar15\Desktop\conf.txt')
f.readline()

rows = f.readlines()
for row in rows:
    col= row.split(',')  #['bucket-111-333434','east-','public']
    new_bucket=col[0]    
    res = get_bucket(new_bucket)
    create_bucket(new_bucket,res)
        

f.close()
