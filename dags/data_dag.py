from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'yongjip',
    'depends_on_past': False,
    'start_date': datetime(2017, 9, 7),
    'email': ['yongjip@sas.upenn.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'update_database', default_args=default_args, schedule_interval=timedelta(minutes=10))

t1 = BashOperator(
    task_id='update_database',
    bash_command='python3 /var/www/projects/trump_project/data/update_db.py',
    dag=dag)
