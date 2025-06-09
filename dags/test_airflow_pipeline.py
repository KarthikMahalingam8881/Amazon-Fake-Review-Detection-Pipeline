from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from datetime import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    description="Test DAG to confirm Airflow 3 is working",
    tags=["test"],
)
def test_airflow_pipeline():
    say_hello = BashOperator(
        task_id='say_hello',
        bash_command='echo "Airflow 3.0 is working ✅"',
    )

    say_hello

test_airflow_pipeline()
