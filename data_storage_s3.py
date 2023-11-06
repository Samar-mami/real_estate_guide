import os

import boto3
from dotenv import load_dotenv


def get_aws_credentials():
    # Load environment variables
    load_dotenv()
    access_key = os.getenv("ACCESS_KEY")
    secret_access_key = os.getenv("SECRET_ACCESS_KEY")
    return access_key, secret_access_key


def connect_aws_s3():
    access_key, secret_access_key = get_aws_credentials()
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)
    return s3


def store_csv_to_s3(bucket, df, object_name):
    s3 = connect_aws_s3()
    csv_buffer = df.to_csv(index=False)
    s3.put_object(Body=csv_buffer, Bucket=bucket, Key=object_name)
    print(f"DataFrame successfully uploaded to S3: s3://{bucket}/{object_name}")
