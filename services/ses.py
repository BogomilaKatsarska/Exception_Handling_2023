import logging

import boto3


class SESService():
    # TODO: Region is not correct
    def __init__(self):
        self.client = boto3.client(
            'ses',
            aws_access_key_id="293850238kJNSGK", 
            aws_secret_access_key="/AJHSFOS2523934",
            region_name='eu-west-1',
        )

    def send_email(self, email):
        logging.info('Starting email sending process')
        response = self.client.send_email(
            Source = 'bogomila@katsarska.com',
            Destination = {
                'ToAddress': [
                    email,
                ],
                'CcAddress': [
                    'string',
                ],
                'BbcAddress': [
                    'string',
                ]
            },
            Message={
                'Subject': {
                    'Data': 'Welcome to our website',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': 'Welcome to our site. Enjoy now. You are registered',
                        'Charset': 'UTF-8'
                    },
                    # 'HTML': {
                    #     'Data': 'x',
                    #     'Charset': 'string'
                    #     }
                }
            },
        )
        logging.info('Email sent')
