from datetime import datetime
from urllib.request import urlopen

SITE = 'http://www.linuxacademy.com'
EXPECTED = 'linux'


def validate(res):
    """Return false if the expected value isn't in the result"""
    return EXPECTED in res


def ping(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        if not validate(str(urlopen(SITE).read())):
            raise Exception('Validation failed')
    except Exception as e:
        print('Check failed!')
        raise e
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))