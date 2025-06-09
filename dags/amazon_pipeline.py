from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from nlp_job.main import run_nlp_pipeline

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id='amazon_nlp_pipeline',
    start_date=datetime(2025, 5, 28),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    tags=["nlp", "s3", "boto3"]
) as dag:

    run_nlp = PythonOperator(
        task_id='run_nlp_pipeline',
        python_callable=run_nlp_pipeline
    )

    run_nlp