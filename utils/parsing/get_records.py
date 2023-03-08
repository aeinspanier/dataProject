import json
import os

def parse_app_version(record):
    app_version_string = record.get('app_version')
    app_version_int = int(app_version_string.replace('.', ''))
    record['app_version'] = app_version_int
    return record
    

def get_records(sqs_client):
    res = sqs_client.read_messages(queue_url=os.environ.get('QUEUE_URL'))
    messages = res.get('Messages')
    body_vals = []
    for message in messages:
        body = json.loads(message.get('Body'))
        record = parse_app_version(body)
        body_vals.append(record)
    
    return body_vals
