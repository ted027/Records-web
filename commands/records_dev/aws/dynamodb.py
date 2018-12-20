import boto3

class dynamodb:
    def __init__(self):
        dynamo = boto3.client('dynamodb')

    def concat_item(HASH_KEY, RANGE_KEY, item_dict):
        dic =  {
            'HASH_KEY': HASH_KEY,
            'RANGE_KEY': RANGE_KEY,
        }
        return dic.update(item_dict)

    def put(table_name, item):
        response = client.put_item(
            TableName=table_name,
            Item=item
        }