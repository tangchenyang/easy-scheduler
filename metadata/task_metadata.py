from models.task.base_task import BaseTask


class TaskMetadata:
    tasks = []

    @staticmethod
    def register(task: BaseTask):
        TaskMetadata.tasks.append(task)

    @staticmethod
    def get_all_tasks():
        return TaskMetadata.tasks

    @staticmethod
    def get_all_tables():
        all_tables = []
        for task in TaskMetadata.tasks:
            all_tables.append(task.output)
            if task.inputs:
                for input_table in task.inputs:
                    all_tables.append(input_table)

        unique_list = list(set(all_tables))
        unique_list.sort()

        return unique_list
