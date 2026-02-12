"""
Unit tests for the Task model.
"""
import unittest
import sys
import os

# Add the src directory to the path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task


class TestTask(unittest.TestCase):
    """Test cases for the Task model."""

    def test_task_creation_with_required_fields(self):
        """Test creating a task with required fields."""
        task = Task(id=1, title="Test Task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)

    def test_task_creation_with_all_fields(self):
        """Test creating a task with all fields."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=True)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertTrue(task.completed)

    def test_task_creation_with_optional_description(self):
        """Test creating a task with optional description."""
        task = Task(id=1, title="Test Task", description="Test Description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)

    def test_task_title_required_validation(self):
        """Test that creating a task with empty title raises an error."""
        with self.assertRaises(ValueError):
            Task(id=1, title="")

        with self.assertRaises(ValueError):
            Task(id=1, title="   ")

    def test_task_default_values(self):
        """Test that task has correct default values."""
        task = Task(id=1, title="Test Task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)


if __name__ == '__main__':
    unittest.main()