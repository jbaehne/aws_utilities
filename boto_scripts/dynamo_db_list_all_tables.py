import os
import boto3

dynamodb_client = boto3.client('dynamodb',
                               aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                               aws_secret_access_key = os.environ.get('AWS_SECRET_KEY'),
                               region_name="us-east-1"
                               )

def list_dynamodb_tables():
    
    table_names = []
    last_evaluated_table_name = None
    
    while True:
        if last_evaluated_table_name:
            response = dynamodb_client.list_tables(ExclusiveStartTableName=last_evaluated_table_name)
        else:
            response = dynamodb_client.list_tables()
        
        table_names.extend(response['TableNames'])
        
        last_evaluated_table_name = response.get('LastEvaluatedTableName')
        
        if not last_evaluated_table_name:
            break
    
    return table_names

if __name__ == '__main__':
    table_names = list_dynamodb_tables()
    for name in table_names:
        print(name)
