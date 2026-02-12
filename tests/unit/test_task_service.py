"""
Unit tests for the TaskService add_task functionality.
"""
import unittest
import sys
import os

# Add the src directory to the path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.task_service import TaskService


class TestTaskService(unittest.TestCase):
    """Test cases for the TaskService."""

    def setUp(self):
        """Set up a fresh TaskService for each test."""
        self.task_service = TaskService()

    def test_add_task_with_title_only(self):
        """Test adding a task with only a title."""
        task = self.task_service.add_task("Test Task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)

    def test_add_task_with_title_and_description(self):
        """Test adding a task with title and description."""
        task = self.task_service.add_task("Test Task", "Test Description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)

    def test_add_multiple_tasks(self):
        """Test adding multiple tasks with auto-incrementing IDs."""
        task1 = self.task_service.add_task("First Task")
        task2 = self.task_service.add_task("Second Task")

        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task1.title, "First Task")
        self.assertEqual(task2.title, "Second Task")

    def test_add_task_returns_task_object(self):
        """Test that add_task returns a Task object."""
        task = self.task_service.add_task("Test Task")
        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Test Task")

    def test_add_task_with_empty_title_raises_error(self):
        """Test that adding a task with empty title raises an error."""
        with self.assertRaises(ValueError):
            self.task_service.add_task("")

        with self.assertRaises(ValueError):
            self.task_service.add_task("   ")

    def test_get_all_tasks_empty(self):
        """Test getting all tasks when there are no tasks."""
        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_get_all_tasks_with_tasks(self):
        """Test getting all tasks when there are tasks."""
        task1 = self.task_service.add_task("First Task", "Description 1")
        task2 = self.task_service.add_task("Second Task", "Description 2")

        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)

    def test_get_all_tasks_after_deletion(self):
        """Test getting all tasks after deleting one."""
        task1 = self.task_service.add_task("First Task")
        task2 = self.task_service.add_task("Second Task")

        self.task_service.delete_task(task1.id)

        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertNotIn(task1, tasks)
        self.assertIn(task2, tasks)

    def test_update_task_success(self):
        """Test successfully updating a task."""
        task = self.task_service.add_task("Original Title", "Original Description")
        updated_task = self.task_service.update_task(task.id, "New Title", "New Description")

        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")

    def test_update_task_partial_update_title(self):
        """Test updating only the title of a task."""
        task = self.task_service.add_task("Original Title", "Original Description")
        updated_task = self.task_service.update_task(task.id, "New Title")

        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "Original Description")

    def test_update_task_partial_update_description(self):
        """Test updating only the description of a task."""
        task = self.task_service.add_task("Original Title", "Original Description")
        updated_task = self.task_service.update_task(task.id, description="New Description")

        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Original Title")
        self.assertEqual(updated_task.description, "New Description")

    def test_update_task_nonexistent_task(self):
        """Test updating a non-existent task."""
        result = self.task_service.update_task(999, "New Title")
        self.assertIsNone(result)

    def test_update_task_with_none_values(self):
        """Test updating a task with None values (should not update those fields)."""
        task = self.task_service.add_task("Original Title", "Original Description")
        updated_task = self.task_service.update_task(task.id, title=None, description=None)

        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Original Title")
        self.assertEqual(updated_task.description, "Original Description")


if __name__ == '__main__':
    unittest.main()