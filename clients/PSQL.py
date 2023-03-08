import psycopg2
from datetime import datetime

def create_record_tuple(record):
    user_id = record.get('user_id')
    device_type = record.get('device_type')
    masked_ip = record.get('ip')
    masked_device_id = record.get('device_id')
    locale = record.get('locale')
    app_version = record.get('app_version')
    create_date = datetime.now()
    
    return (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
    

class PSQL:
    def __init__(self, dbname, user, password):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password)
        self.cursor = self.conn.cursor()
        
        self.create_table_if_not_exist()
    
    
    def create_table_if_not_exist(self):
        psql_query = """
        CREATE TABLE IF NOT EXISTS user_logins(
            user_id VARCHAR(128),
            device_type VARCHAR(32),
            masked_ip VARCHAR(256),
            masked_device_id VARCHAR(256),
            locale VARCHAR(32),
            app_version INT,
            create_date DATE
        );
        """
        try:
            self.cursor.execute(psql_query)
            self.conn.commit()
        except Exception as e:
            print(e)
    
    def insert_record(self, record_tuple):
        postgres_insert_query = """ INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        
        try:
            self.cursor.execute(postgres_insert_query, record_tuple)
            self.conn.commit()
        except Exception as err:
            print(err)
    
    
    def write_records(self, records):
        for record in records:
            record_tuple = create_record_tuple(record)
            self.insert_record(record_tuple)
            