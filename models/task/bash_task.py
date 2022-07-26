from enums.task_enums import TaskType
from models.task.base_task import BaseTask


class BashTask(BaseTask):

    def __init__(self,
                 bash_command="echo bash task !!!",  # todo
                 *args,
                 **kwargs):
        super(BashTask, self).__init__(*args, **kwargs)
        self.task_type = TaskType.BASH
        self.bash_command = bash_command
