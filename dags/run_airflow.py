from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id = "smartup_elt",
    description = "pipeline.py ni ishga tushiradi",
    start_date = datetime(2025, 1, 1),
    schedule = "0 3 * * *", # har kuni soat 3 da
    catchup = False,
    default_args = {
        "owner": "golibjon",
        "retries": 2,
        "retry_delay": timedelta(minutes=5)
    },
    tags = ['elt', 'smartup']
) as dag:

    run_pipline = BashOperator(
        task_id = "run_pipline",
        bash_command = "python /opt/airflow/smartup_elt/pipline.py" # Papka yo'lini o'zingiznikiga moslab qo'yasiz
    )