import boto3

class dynamodb:
    def __init__(self):
        dynamo = boto3.client('dynamodb')

    def put(HASH_KEY, RANGE_KEY):
        response = client.put_item(
            TableName=table_name,
            Item=item
        }