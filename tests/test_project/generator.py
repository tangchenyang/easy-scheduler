from adapter.airflow.airflow_generator import AirflowGenerator

generator = AirflowGenerator()
generator.generate(config_dir='/Users/chenyang.tang-fox/IdeaProjects/chenyang.tang/easy-scheduler/tests/test_project/confs',
                   target_dir='/Users/chenyang.tang-fox/IdeaProjects/chenyang.tang/easy-scheduler/tests/test_project/pipeline_test_project.py')