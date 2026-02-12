#!/usr/bin/env python3
"""
Main CLI application for the Todo app.
"""
import sys
import os
from typing import Optional

# Add the src directory to the path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.task_service import TaskService


class TodoCLI:
    """
    CLI interface for the Todo application.
    """

    def __init__(self):
        """Initialize the CLI with a task service."""
        self.task_service = TaskService()

    def display_menu(self):
        """Display the main menu options."""
        print("\nTodo Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Complete")
        print("6. Exit")

    def get_user_choice(self) -> int:
        """
        Get and validate user menu choice.

        Returns:
            The user's menu choice as an integer
        """
        while True:
            try:
                choice = input("Choose an option: ").strip()
                if not choice:
                    print("Invalid input. Please enter a number between 1-6.")
                    continue
                choice = int(choice)
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Invalid input. Please enter a number between 1-6.")
            except ValueError:
                print("Invalid input. Please enter a number between 1-6.")

    def add_task(self):
        """Handle adding a new task."""
        title = input("Enter task title: ").strip()
        if not title:
            print("Title is required.")
            return

        description = input("Enter task description (optional): ").strip()
        task = self.task_service.add_task(title, description)
        print(f"Task added successfully with ID: {task.id}")

    def view_tasks(self):
        """Handle viewing all tasks."""
        tasks = self.task_service.get_all_tasks()
        if not tasks:
            print("No tasks found.")
            return

        print("\nTasks:")
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"ID: {task.id}, Title: {task.title}, Status: {status}")
            if task.description:
                print(f"  Description: {task.description}")

    def update_task(self):
        """Handle updating a task."""
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid ID. Please enter a valid task ID.")
            return

        task = self.task_service.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} does not exist.")
            return

        new_title = input(f"Enter new title (leave blank to keep '{task.title}'): ").strip()
        new_description = input(f"Enter new description (leave blank to keep '{task.description}'): ").strip()

        # Use current values if user entered blank
        title = new_title if new_title else None
        description = new_description if new_description else None

        updated_task = self.task_service.update_task(task_id, title, description)
        if updated_task:
            print("Task updated successfully")
        else:
            print("Failed to update task")

    def delete_task(self):
        """Handle deleting a task."""
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a valid task ID.")
            return

        success = self.task_service.delete_task(task_id)
        if success:
            print("Task deleted successfully")
        else:
            print(f"Task with ID {task_id} does not exist.")

    def toggle_task_completion(self):
        """Handle toggling task completion status."""
        try:
            task_id = int(input("Enter task ID to toggle: "))
        except ValueError:
            print("Invalid ID. Please enter a valid task ID.")
            return

        task = self.task_service.toggle_task_completion(task_id)
        if task:
            status = "completed" if task.completed else "incomplete"
            print(f"Task completion status updated. Now {status}.")
        else:
            print(f"Task with ID {task_id} does not exist.")

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Application!")
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.update_task()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                self.toggle_task_completion()
            elif choice == 6:
                print("Goodbye!")
                sys.exit(0)


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()