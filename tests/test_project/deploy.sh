current_dir=$(cd `dirname $0` && pwd)

AIRFLOW_DAG_PATH='/Users/chenyang.tang-fox/airflow/dags'

cmd="cp -r $current_dir/pipeline_test_project.py $AIRFLOW_DAG_PATH"
echo "${cmd}"
eval "${cmd}"