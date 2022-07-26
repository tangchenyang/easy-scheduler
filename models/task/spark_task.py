from enums.task_enums import TaskType
from models.task.base_task import BaseTask


class SparkTask(BaseTask):

    def __init__(self,
                 jar="",
                 *args,
                 **kwargs):
        super(SparkTask, self).__init__(*args, **kwargs)
        self.task_type = TaskType.SPARK
        self.jar = jar
