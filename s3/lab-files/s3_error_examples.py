import boto3

s3 = boto3.resource('s3')

def try_to_get_object(bucket, key):
    try:
        obj = s3.Object(bucket, key)
        return obj.get()['Body'].read().decode('utf-8')
    except Exception as e:
        print('Error:')
        print(e)

# Access denied error
no_access_bucket = 'www.fernandomc.com'
no_access_key = 'index.html'
try_to_get_object(no_access_bucket, no_access_key)

# No such key
exisiting_bucket = '<REPLACE WITH YOUR BUCKET>'
fake_key = 'something.something.not.real'
try_to_get_object(exisiting_bucket, fake_key)

# No such bucket
imaginary_bucket = 'please.dont.make.this.a.real.bucket.or.the.example.will.fail'
imaginary_bucket_key = 'something.something.not.real'
try_to_get_object(imaginary_bucket, imaginary_bucket_key)

# Invalid bucket name
invalid_bucket_name = '<!Mycoolbucketnamethatwontwork!>'
invalid_bucket_key = 'somefilename'
try_to_get_object(invalid_bucket_name, invalid_bucket_key)
