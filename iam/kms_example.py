import boto3

kms = boto3.client('kms')
key_id = 'alias/tempKey'
database_password = 'SOME_PASSWORD_OR_SECRET'

result = kms.encrypt(KeyId=key_id, Plaintext=database_password)

print(result)

encrypted_password = result['CiphertextBlob']

print(encrypted_password)

decrypt_result = kms.decrypt(CiphertextBlob=encrypted_password)

decrypt_result['Plaintext']