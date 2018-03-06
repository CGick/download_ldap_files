import boto3
import json

s3 = boto3.client('s3')

bucket_name = 'sftp-openldap-config-files'
path = "/tmp/ldap-files/"

objects = [var['Key'] for var in s3.list_objects(Bucket=bucket_name)['Contents']]
    
for item in objects:
    file_path = path + item
    with open(file_path, 'wb') as infile:
        s3.download_fileobj(bucket_name, item, infile)
