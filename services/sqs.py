from datetime import datetime

import boto3


class SQSService:
    def __init__(self):
        self.url = 'https://sqs.eu-west-1.amazonaws.com/36253...'
        self.client = boto3.client(
            'sqs',
            aws_access_key_id="293850238kJNSGK",
            aws_secret_access_key="/AJHSFOS2523934",
            region_name='eu-west-1',
        )

    def send_message(self, email):
        self.client.send_message(
            QueueUrl=self.url,
            MessageBody=f'sending mail to {email}',
            DelaySeconds=0,
            # MessageAttributes={
            #     We fill this if we need any additional attributes to our message
            # },
            MessageDeduplicationId=str(datetime.utcnow().timestamp()),
            MessageGroupId=str(datetime.utcnow().timestamp()),
        )