import boto3
import os

Access_key_ID='AKIAXM7XUAWH6VK2EDRJ'
Secret_access_key='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'

s3 = boto3.client('s3',aws_access_key_id=Access_key_ID,aws_secret_access_key=Secret_access_key)

name ='mydata-1001113-test'
s3.create_bucket(Bucket=name)
print('Bucket is created')


#upload file
os.chdir(r'C:\Users\vkumar15\Desktop\folder')

res = os.listdir()
print(res)
for f in res:
    #print(f)
    #print(os.path.isdir(f) )
    #if f.count('.')>0:  #f.endswith('.txt'):
    if os.path.isdir(f) == False:
        s3.upload_file(f, name, f)
        
        
        

'''
fname ='Python Boto3.docx'

s3.upload_file(fname, name, fname)
print(' uploaded ')

'''
