from aws_lambda_powertools import Logger


log = Logger("handler")


def handler(event, context):
    
    for message in event["Records"]:
        log.info(f"the message is {message}")