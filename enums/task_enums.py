import enum


@enum.unique
class TaskType(enum.Enum):
    SPARK = "spark"
    PYTHON = "python"
    HIVE = "hive"
    ATHENA = "athena"
    BASH = "bash"

    @staticmethod
    def value_of(task_type_str: str):
        if task_type_str is None:
            raise Exception(f"task_type should not be None.")

        for name, member in TaskType.__members__.items():
            if task_type_str.lower() == member.value:
                return member

        raise Exception(f"Unsupported TaskType: {task_type_str}. "
                        f"Only support [{'/'.join(TaskType.__members__.keys())}]")
