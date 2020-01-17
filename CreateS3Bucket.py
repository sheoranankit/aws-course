import boto3

Access_key_ID='AKIAXM7XUAWH2HT6EAMM'
Secret_access_key='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'


o = boto3.client('s3',aws_access_key_id=Access_key_ID,aws_secret_access_key=Secret_access_key)

#new_bucket ='data-migrration-11110222033444'
new_bucket = input('enter bucket name :')

is_exist =  False
#get list of existing buckets 
res = o.list_buckets()

for b in res['Buckets']:
    #print(b['Name'])
    if new_bucket ==b['Name']:
        is_exist = True
    
    


if is_exist == False:
    o.create_bucket(Bucket=new_bucket)
    print('Bucket is created ')
else:
    print(new_bucket,' is already exist')
    












