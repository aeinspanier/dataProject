

def mask_ip_address(record):
    ip = record.get('ip')
    ip_arr = ip.split('.')
    ip_arr.reverse()
    masked_ip = '.'.join(ip_arr)
    record['ip'] = masked_ip

def mask_device_id(record):
    device_id = record.get('device_id')
    id_arr = device_id.split('-')
    id_arr.reverse()
    masked_id = '-'.join(id_arr)
    record['device_id'] = masked_id

def mask_fields(records):
    for record in records:
        mask_ip_address(record)
        mask_device_id(record)
    return records
