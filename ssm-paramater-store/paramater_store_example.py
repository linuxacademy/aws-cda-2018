# This code is written for Python3. 
# To use this code for Python2 simply:
# change the print() functions to
# print statenents
import boto3 

ssm = boto3.client('ssm')

response = ssm.put_parameter(
    Name='test2',
    Description='The password for the Dev MySQL DB',
    Value='super-secret-password,test',
    Type='StringList'
)

print(response)

decrypted_value_response = ssm.get_parameter(
    Name='test2',
    WithDecryption=True
)

print(decrypted_value_response)
