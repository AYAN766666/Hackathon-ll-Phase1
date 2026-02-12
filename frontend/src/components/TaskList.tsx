
// components/TaskList.tsx
import { useState } from 'react';
import TaskItem from './TaskItem';
import { Task } from '@/src/services/api';

interface TaskListProps {
  tasks: Task[];
  onTaskUpdated: (task: Task) => void;
  onTaskDeleted: (taskId: number) => void;
  onTaskToggled: (taskId: number, completed: boolean) => void;
}

export default function TaskList({ tasks, onTaskUpdated, onTaskDeleted, onTaskToggled }: TaskListProps) {
  const safeTasks = tasks.filter((task): task is Task => task !== null && task !== undefined);

  if (safeTasks.length === 0) {
    return (
      <div className="bg-white px-4 py-16 sm:px-6 lg:px-8 rounded-lg border-2 border-dashed border-gray-200">
        <div className="text-center animate-fade-in">
          <h3 className="mt-4 text-lg font-medium text-gray-900">No tasks yet</h3>
          <p className="mt-2 text-sm text-gray-500">Get started by creating your first task.</p>
        </div>
      </div>
    );
  }

  return (
    <ul className="divide-y divide-gray-200">
      {safeTasks.map((task, index) => (
        <li key={task.id} className={` ${index === 0 ? 'animate-fade-in' : ''}`} style={{ animationDelay: `${index * 0.1}s` }}>
          <TaskItem
            task={task}
            onTaskUpdated={onTaskUpdated}
            onTaskDeleted={onTaskDeleted}
            onTaskToggled={onTaskToggled}
          />
        </li>
      ))}
    </ul>
  );
}
