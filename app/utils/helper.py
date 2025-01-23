def serialize_account_data(data):
    serialized_data = []
    for item in data:
        serialized_item = {
            'id': item[0],
            'account_name': item[1],
            'account_number': item[2],
            'balance': float(item[3])
        }
        serialized_data.append(serialized_item)
    return serialized_data

def serialize_txn_data(data):
    serialized_data = []
    for item in data:
        serialized_item = {
            'id': item[0],
            'transaction_date': item[1].isoformat(),
            'from_account': item[2],
            'to_account': item[3],
            'transaction_amount': float(item[4]),
            'remarks':item[5]
        }
        serialized_data.append(serialized_item)
        
    return serialized_data