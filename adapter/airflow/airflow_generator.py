import os

from adapter.airflow.template import template
from adapter.base_generator import BaseGenerator
from confparser.json_parser import JsonParser
from enums.task_enums import TaskType
from models.task.base_task import BaseTask


class AirflowGenerator(BaseGenerator):

    def __read_file(self, file):
        f = open(file, "r")
        query = f.read()
        return query

    def generate(self, config_dir, target_dir):
        # 1. read task from metadata
        config_files = os.listdir(config_dir)
        config_contents = [self.__read_file(f'{config_dir}/{file}') for file in config_files]  # read from file
        tasks = [JsonParser().parse(json_str) for json_str in config_contents]

        base_dag_part = self.__draw_base_part()

        tasks_part = '\n'.join([self.draw_task(task) for task in tasks])

        dependency_part = '\n'.join([self.draw_dependency(task) for task in tasks])

        dag_content = f"""
           {base_dag_part}

           {tasks_part}

           {dependency_part}
           """

        with open(target_dir, 'w') as f:
            f.write(dag_content)

    def __draw_base_part(self):
        base_dag_part = template.base_dag_part.format(dag_id="test_dag")
        return base_dag_part

    def draw_task(self, task):
        if task.task_type == TaskType.BASH:
            task_content = template.bash_task_template.format(task_name=task.task_name,
                                                              bash_command=task.bash_command)
        else:
            task_content = ""

        return task_content

    def draw_dependency(self, task: BaseTask):
        if task.inputs:
            return f""
        else:
            return ""
