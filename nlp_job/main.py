import boto3
from nlp_job.s3_helpers import load_parquet_from_s3, save_parquet_to_s3
from nlp_job.nlp_processing import clean_text_column, apply_sentiment

def run_nlp_pipeline():
    bucket = "amazon-fake-reviews-data"
    prefix = "processed/year=2023/"
    output_prefix = "processed/nlp/year=2023/"

    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith(".parquet"):
            print(f"Processing {key}...")
            try:
                # Load only required column to save memory
                df = load_parquet_from_s3(bucket, key, columns=['text'])
                df = clean_text_column(df, text_column='text')
                df = apply_sentiment(df, text_column='text')

                output_key = output_prefix + key.split('/')[-1].replace(".parquet", "_nlp.parquet")
                save_parquet_to_s3(df, bucket, output_key)
                print(f"Saved processed file to {output_key}")
            except Exception as e:
                print(f"Failed to process {key}: {e}")