import boto3
sns = boto3.client('sns')
your_phone_number = '+1555777####'
sns.publish(Message='Hello', PhoneNumber=your_phone_number)