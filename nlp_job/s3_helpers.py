import boto3
import pyarrow.parquet as pq
import io
import os
import pandas as pd

def load_parquet_from_s3(bucket, key, columns=None):
    """
    Load Parquet file from S3 using pyarrow with optional column selection.
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    response = s3.get_object(Bucket=bucket, Key=key)
    body = response['Body'].read()
    buf = io.BytesIO(body)

    table = pq.read_table(buf, columns=columns)
    return table.to_pandas()

def save_parquet_to_s3(df, bucket, key):
    """
    Save Pandas DataFrame to S3 as a Parquet file.
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )
    out_buffer = io.BytesIO()
    df.to_parquet(out_buffer, index=False)
    s3.put_object(Bucket=bucket, Key=key, Body=out_buffer.getvalue())