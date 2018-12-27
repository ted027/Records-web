import boto3

class dynamodb:
    def __init__(self, table_name):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(table_name)

    def concat_item(self, HASH_KEY, RANGE_KEY, item_dict):
        dic =  {
            'HASH_KEY': HASH_KEY,
            'RANGE_KEY': RANGE_KEY,
        }
        return dic.update(item_dict)

    def put(self, item):
        self.table.put_item(
            Item=item
        )

    def batch_write_item(self, HASH_KEY, items):
        with self.table.batch_writer() as batch:
            for item in items:
                RANGE_KEY = item.pop('年度')
                item_dict = self.concat_item(HASH_KEY, RANGE_KEY, item)
                batch.put_item(Item =item_dict)