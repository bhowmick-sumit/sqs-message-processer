from aws_lambda_powertools import Logger
from aws_lambda_powertools.metrics import Metrics
import os
import json
import boto3
from datetime import datetime


log = Logger("handler")
s3_resource = boto3.resource("s3")
BUCKET_NAME = os.getenv("DESTINATION_BUCKET_NAME") 


metric = Metrics()


@metric.log_metrics
def handler(event, context):
    log.info(f"event: {event}")

    for record in event["Records"]:
        message = record["body"]
        metric.add_metric(name="messagesRecived", unit="Count", value=1)
        fileName = json.loads(message).get("fileName")
        if fileName != None:
            metric.add_metadata(name="messageSuccessful", unit="Count", value=1)
            log.info(f"the message is {message}")
            s3_resource.Bucket(BUCKET_NAME).put_object(Key=fileName,Body=message)
        else:
            metric.add_metric(name="messageFailed", unit="Count", value=0)
            raise "fileName not found"
        
