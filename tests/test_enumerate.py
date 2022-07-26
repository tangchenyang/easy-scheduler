from unittest import TestCase

from enums.task_enums import TaskType


class TestTaskType(TestCase):

    def test_value_of(self):
        self.assertEqual(TaskType.value_of("spark"), TaskType.SPARK)
        self.assertEqual(TaskType.value_of("python"), TaskType.PYTHON)
        self.assertEqual(TaskType.value_of("hive"), TaskType.HIVE)
        self.assertEqual(TaskType.value_of("athena"), TaskType.ATHENA)
        self.assertEqual(TaskType.value_of("bash"), TaskType.BASH)

        with self.assertRaises(Exception):
            TaskType.value_of("other")
