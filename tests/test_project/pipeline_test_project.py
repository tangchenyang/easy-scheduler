
           
from airflow import DAG
from datetime import datetime, timedelta

now = datetime.now()
two_days_ago = now - timedelta(days=2, seconds=now.second, microseconds=now.microsecond)
 
dag = DAG(dag_id='test_dag',
          start_date=two_days_ago) 


           
from airflow.operators.bash_operator import BashOperator
task1 = BashOperator(
    task_id='task1',
    bash_command='echo !',
    dag=dag
)


           
           