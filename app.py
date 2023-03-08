from utils.parsing.get_records import get_records
from utils.masking.mask_fields import mask_fields
from clients.SQSClient import SQSClient
from clients.PSQL import PSQL
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())



if __name__ == "__main__":
    print(os.environ.get('QUEUE_URL'))
    sqs_client = SQSClient()
    psql_client = PSQL(dbname=os.environ.get("PSQL_DB"),
                       user=os.environ.get("PSQL_USER"),
                       password=os.environ.get("PSQL_PASSWORD"))
    records = get_records(sqs_client)
    masked_records = mask_fields(records)
    psql_client.write_records(masked_records)
    
