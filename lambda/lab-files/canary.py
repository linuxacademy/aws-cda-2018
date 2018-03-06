import boto3
import os
from datetime import datetime
from urllib.request import urlopen

sns = boto3.client('sns')

# Make sure to add these in the Lambda Console
SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable
EXPECTED = os.environ['expected']  # String expected to be on the page, stored in the expected environment variable


def send_text(status):
    sns.publish(
        Message=(
            'Hello! Your website check for {0} has {1}'.format(
                SITE, 
                status
            )
        ), 
        PhoneNumber='+15556668888'
    )


def validate(res):
    """Return false if the expected value isn't in the result"""
    return EXPECTED in res


def lambda_handler(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        if not validate(str(urlopen(SITE).read())):
            send_text('failed')
            raise Exception('Validation failed')
    except:
        print('Check failed!')
        send_text('failed')
        raise
    else:
        print('Check passed!')
        send_text('passed')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))