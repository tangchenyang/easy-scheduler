import json

from confparser.base_parser import BaseParser
from enums.task_enums import TaskType
from models.task.bash_task import BashTask


class JsonParser(BaseParser):

    def __init__(self):
        super().__init__()

    def parse(self, json_str):
        _dict = json.loads(json_str)
        task_type = TaskType.value_of(_dict['task_type'])

        if task_type == TaskType.BASH:
            return BashTask(bash_command="echo !", task_name=_dict['task_name'])
        else:
            raise Exception("Only support BASH !!!")  # todo
