
base_dag_part = """
from airflow import DAG
from datetime import datetime, timedelta

now = datetime.now()
two_days_ago = now - timedelta(days=2, seconds=now.second, microseconds=now.microsecond)
 
dag = DAG(dag_id='{dag_id}',
          start_date=two_days_ago) 
"""

processing_part = """
from airflow.operators.python_operator import PythonOperator
from {class_package_path} import {class_name}
{task_name} = PythonOperator(task_id='{task_name}',
                             python_callable={class_name}().process,
                             dag=dag) 
"""

check_result_part = """
from airflow.operators.python_operator import PythonOperator
from {class_package_path} import {class_name}
{task_name} = PythonOperator(task_id='{task_name}',
                             python_callable={class_name}().check_result,
                             dag=dag) 
"""

bash_task_template = """
from airflow.operators.bash_operator import BashOperator
{task_name} = BashOperator(
    task_id='{task_name}',
    bash_command='{bash_command}',
    dag=dag
)
"""