import boto3
import os

class SQSClient:
    def __init__(self):
        self.sqs_client = boto3.client('sqs', endpoint_url=os.environ.get('ENDPOINT_URL'))
    
    def read_messages(self, queue_url, attribute_names=['All'], max_num_messages=10 ):
        return self.sqs_client.receive_message(QueueUrl=queue_url,
                                AttributeNames=attribute_names,
                                MaxNumberOfMessages=max_num_messages)


