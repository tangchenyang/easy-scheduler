import json
from typing import List

from enums.task_enums import TaskType


class BaseTask:
    def __init__(self,
                 task_name: str = None,
                 task_type: TaskType = TaskType.PYTHON,
                 inputs: List[str] = None,  # todo 表名用实体代替
                 output: str = None,  # todo 表名用实体代替
                 ):
        self.task_name = task_name
        self.task_type = task_type
        self.inputs = inputs
        self.output = output

    def process(self):
        raise Exception(f"should implement this function")

    def check_result(self):
        print(f'check result for {self.task_name}')

