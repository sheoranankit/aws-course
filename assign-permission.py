import json
import boto3

bucket_name = 'mydata-1001113-test-03'

#print('bucket name is {} test'.format(bucket_name))

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

#print(bucket_policy)
# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)
#print(bucket_policy)

Access_key_ID='AKIAXM7XUAWH6VK2EDRJ'
Secret_access_key='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'

s3 = boto3.client('s3',aws_access_key_id=Access_key_ID,aws_secret_access_key=Secret_access_key)

s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
print(' given plicy is assigned')




