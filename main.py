from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import boto3
from botocore.client import Config
import logging
import json
from botocore.exceptions import ClientError


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

driver.get('http://localhost:4444/grid/console')

# to take the screenshot

driver.get_screenshot_as_file('screenshot2.png')


# sending the screenshot into s3

ACCESS_KEY_ID = 'AKIA5N2WSCDUEBR4FEYL'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'gird-screenshot'

data = open('screenshot2.png', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='screenshot2.png', Body=data)

print("Done")


def create_presigned_url(bucket_name, object_name, fields=None, conditions=None, expiration=30):
    my_config = Config(
        region_name='ap-south-1',
        signature_version='s3v4',
    )

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


result = create_presigned_url("gird-screenshot", "screenshot2.png")

print(json.dumps(result, indent=4))
