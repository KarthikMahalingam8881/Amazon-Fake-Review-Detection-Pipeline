from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.glue import GlueCrawlerOperator, GlueJobOperator
from datetime import datetime, timedelta
import os

from scripts.extract_from_s3 import extract_data
from scripts.run_nlp import process_nlp
from scripts.upload_to_s3 import upload_data
from nlp_job.main import run_nlp_pipeline

# Default arguments for all tasks
default_args = {
    'owner': 'karthik',
    'start_date': datetime(2025, 5, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email': ['kmahali2@asu.edu']
}

# Define the DAG
with DAG(
    dag_id='amazon_review_etl_full_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    # Step 1: Upload raw review data to S3 (placeholder logic)
    def upload_raw():
        print("Uploading raw review file to S3...")
        # Add boto3 code here if automating ingestion

    upload_raw_task = PythonOperator(
        task_id='upload_raw_to_s3',
        python_callable=upload_raw
    )

    # Step 2: Trigger Glue Crawler to infer schema
    glue_crawler_task = GlueCrawlerOperator(
        task_id='run_glue_crawler',
        config={"Name": "amazon-reviews-crawler"},
        aws_conn_id='aws_default'
    )

    # Step 3: Run Glue ETL Spark job to transform JSONL to Parquet
    glue_etl_task = GlueJobOperator(
        task_id='run_glue_etl_job',
        job_name='amazon-etl-job',
        script_location='s3://amazon-glue-scripts/transform.py',
        aws_conn_id='aws_default',
        region_name='us-east-2'
    )

    # Step 4: Download processed Parquet files from S3
    extract_parquet_task = PythonOperator(
        task_id='extract_parquet_from_s3',
        python_callable=extract_data
    )

    # Step 5: NLP Processing (lemmatization + sentiment)
    nlp_processing_task = PythonOperator(
        task_id='run_nlp_cleaning',
        python_callable=process_nlp
    )

    # Step 6: Upload enriched result back to S3
    upload_results_task = PythonOperator(
        task_id='upload_processed_to_s3',
        python_callable=upload_data
    )

    # dependencies
    upload_raw_task >> glue_crawler_task >> glue_etl_task >> extract_parquet_task >> nlp_processing_task >> upload_results_task
