#cloud setup

from CreateS3Bucket_2 import *



while True:
    ch =input('enter 1 for new bucket 2 for get list of existing bucket and 0 for exit')
    if ch=='1':        
        #get input
        new_bucket = input('enter bucket name :')
        res = get_bucket(new_bucket)
        create_bucket(new_bucket,res)
    elif ch=='2':
        res = get_bucket(new_bucket,'show')

    elif ch =='0':
        break
    else:
        print('invalid choice, plz try again !!!')

        


