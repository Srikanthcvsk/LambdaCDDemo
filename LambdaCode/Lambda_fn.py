import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    print("Big decisions")
    print(" Testing Code Pipeline")
    
    return {"statusCode": 200, "body": json.dumps(response)}
