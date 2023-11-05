from aws_lambda_powertools import Logger
import os
import json
import boto3
from datetime import datetime


log = Logger("handler")
s3_resource = boto3.resource("s3")
BUCKET_NAME = os.getenv("DESTINATION_BUCKET_NAME") 


def handler(event, context):
    log.info("event: {event}")

    for record in event["Records"]:
        message = record["body"]
        fileName = json.loads(message).get("fileName")
        if fileName != None:
            log.info(f"the message is {message}")
            # s3_resource.Bucket(BUCKET_NAME).put_object(Key=fileName,Body=message)

        else:
            raise "fileName not found"