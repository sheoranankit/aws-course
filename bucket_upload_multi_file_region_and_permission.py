import boto3
import os

Access_key_ID='AKIAXM7XUAWH6VK2EDRJ'
Secret_access_key='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'

region ='ap-south-1'

s3 = boto3.client('s3',region_name=region,aws_access_key_id=Access_key_ID,aws_secret_access_key=Secret_access_key)

name ='mydata-1001113-test-039'

#change the locaiton 
location = {'LocationConstraint': region}
s3.create_bucket(Bucket=name,CreateBucketConfiguration=location)

print(name,' is created in region ',region)

###





