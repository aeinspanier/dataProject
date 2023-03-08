import boto3
import os

def get_queue_msg():
    sqs = boto3.client('sqs', endpoint_url=os.environ.get('ENDPOINT_URL'))
    res = sqs.receive_message(QueueUrl=os.environ.get('QUEUE_URL'))
    print(res)
