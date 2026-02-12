"""
Integration tests for the CLI View Tasks functionality.
"""
import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the src directory to the path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.cli.main import TodoCLI


class TestCLIViewTasks(unittest.TestCase):
    """Integration tests for the CLI View Tasks functionality."""

    def setUp(self):
        """Set up a fresh CLI for each test."""
        self.cli = TodoCLI()

    def test_view_tasks_with_tasks(self):
        """Test viewing tasks when there are tasks."""
        # Add a task first
        cli_with_task = TodoCLI()
        cli_with_task.task_service.add_task("Test Task", "Test Description")

        # Capture the output when viewing tasks
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        cli_with_task.view_tasks()

        # Restore stdout
        sys.stdout = original_stdout

        output = captured_output.getvalue()
        self.assertIn("Test Task", output)
        self.assertIn("Test Description", output)
        self.assertIn("Pending", output)

    @patch('builtins.input', side_effect=['6'])
    def test_view_tasks_empty_list(self, mock_input):
        """Test viewing tasks when there are no tasks."""
        # Reset CLI to have a fresh service
        cli_empty = TodoCLI()

        # Capture the output when viewing tasks
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        cli_empty.view_tasks()

        # Restore stdout
        sys.stdout = original_stdout

        output = captured_output.getvalue()
        self.assertIn("No tasks found.", output)

    def test_update_task_cli_flow(self):
        """Test the CLI flow for updating a task."""
        # Create CLI and add a task first
        cli = TodoCLI()
        task = cli.task_service.add_task("Original Task", "Original Description")

        # Patch input to simulate user interaction
        with patch('builtins.input', side_effect=[str(task.id), "Updated Task", "Updated Description"]):
            # Capture the output
            captured_output = StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_output

            cli.update_task()

            # Restore stdout
            sys.stdout = original_stdout

            output = captured_output.getvalue()
            self.assertIn("Task updated successfully", output)

        # Verify the task was actually updated in the service
        updated_task = cli.task_service.get_task_by_id(task.id)
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertEqual(updated_task.description, "Updated Description")

    def test_update_task_cli_invalid_id(self):
        """Test the CLI flow for updating a non-existent task."""
        cli = TodoCLI()

        # Patch input to simulate user entering invalid ID
        with patch('builtins.input', side_effect=['999']):
            # Capture the output
            captured_output = StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_output

            cli.update_task()

            # Restore stdout
            sys.stdout = original_stdout

            output = captured_output.getvalue()
            self.assertIn("does not exist", output)

    def test_get_all_tasks_returns_all_tasks(self):
        """Test that get_all_tasks returns all added tasks."""
        # Add some tasks
        task1 = self.cli.task_service.add_task("Task 1", "Description 1")
        task2 = self.cli.task_service.add_task("Task 2", "Description 2")
        task3 = self.cli.task_service.add_task("Task 3", "Description 3")

        # Get all tasks
        all_tasks = self.cli.task_service.get_all_tasks()

        # Verify all tasks are returned
        self.assertEqual(len(all_tasks), 3)
        self.assertIn(task1, all_tasks)
        self.assertIn(task2, all_tasks)
        self.assertIn(task3, all_tasks)

    def test_delete_task_cli_flow(self):
        """Test the CLI flow for deleting a task."""
        # Create CLI and add a task first
        cli = TodoCLI()
        task = cli.task_service.add_task("Task to Delete", "Description to Delete")

        # Verify task exists before deletion
        initial_tasks = cli.task_service.get_all_tasks()
        self.assertEqual(len(initial_tasks), 1)

        # Patch input to simulate user interaction for deletion
        with patch('builtins.input', side_effect=[str(task.id)]):
            # Capture the output
            captured_output = StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_output

            cli.delete_task()

            # Restore stdout
            sys.stdout = original_stdout

            output = captured_output.getvalue()
            self.assertIn("Task deleted successfully", output)

        # Verify the task was actually deleted from the service
        remaining_tasks = cli.task_service.get_all_tasks()
        self.assertEqual(len(remaining_tasks), 0)

    def test_delete_task_cli_invalid_id(self):
        """Test the CLI flow for deleting a non-existent task."""
        cli = TodoCLI()

        # Patch input to simulate user entering invalid ID
        with patch('builtins.input', side_effect=['999']):
            # Capture the output
            captured_output = StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_output

            cli.delete_task()

            # Restore stdout
            sys.stdout = original_stdout

            output = captured_output.getvalue()
            self.assertIn("does not exist", output)

    def test_toggle_task_completion_cli_flow(self):
        """Test the CLI flow for toggling task completion."""
        # Create CLI and add a task first
        cli = TodoCLI()
        task = cli.task_service.add_task("Task to Toggle", "Description for Toggle")

        # Verify task is initially not completed
        self.assertFalse(task.completed)

        # Patch input to simulate user interaction for toggling
        with patch('builtins.input', side_effect=[str(task.id)]):
            # Capture the output
            captured_output = StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_output

            cli.toggle_task_completion()

            # Restore stdout
            sys.stdout = original_stdout

            output = captured_output.getvalue()
            self.assertIn("completed", output)

        # Verify the task was actually updated in the service
        updated_task = cli.task_service.get_task_by_id(task.id)
        self.assertIsNotNone(updated_task)
        self.assertTrue(updated_task.completed)

        # Toggle again to make it incomplete
        with patch('builtins.input', side_effect=[str(task.id)]):
            # Capture the output
            captured_output = StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_output

            cli.toggle_task_completion()

            # Restore stdout
            sys.stdout = original_stdout

            output = captured_output.getvalue()
            self.assertIn("incomplete", output)

        # Verify the task was updated to incomplete
        updated_task = cli.task_service.get_task_by_id(task.id)
        self.assertIsNotNone(updated_task)
        self.assertFalse(updated_task.completed)

    def test_toggle_task_completion_cli_invalid_id(self):
        """Test the CLI flow for toggling completion of a non-existent task."""
        cli = TodoCLI()

        # Patch input to simulate user entering invalid ID
        with patch('builtins.input', side_effect=['999']):
            # Capture the output
            captured_output = StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_output

            cli.toggle_task_completion()

            # Restore stdout
            sys.stdout = original_stdout

            output = captured_output.getvalue()
            self.assertIn("does not exist", output)


if __name__ == '__main__':
    unittest.main()