
'use client';

import { useState } from 'react';
import { Task } from '@/src/services/api';

interface TaskItemProps {
  task: Task;
  onTaskUpdated: (task: Task) => void;
  onTaskDeleted: (taskId: number) => void;
  onTaskToggled: (taskId: number, completed: boolean) => void;
}

export default function TaskItem({
  task,
  onTaskUpdated,
  onTaskDeleted,
  onTaskToggled,
}: TaskItemProps) {
  const [loading, setLoading] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const [editDescription, setEditDescription] = useState(task.description || '');
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [showViewModal, setShowViewModal] = useState(false);

  // Toggle complete
  const handleToggle = async () => {
    setLoading(true);
    try {
      await onTaskToggled(task.id, !task.completed);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Delete task
  const handleDelete = async () => {
    setLoading(true);
    try {
      await onTaskDeleted(task.id);
      setShowDeleteModal(false);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Edit task
  const handleEdit = () => {
    setIsEditing(true);
    setEditTitle(task.title);
    setEditDescription(task.description || '');
  };

  const handleSave = async () => {
    if (!editTitle.trim()) return;
    setLoading(true);
    try {
      const apiService = (await import('@/src/services/api')).default;
      const updatedTask = (await apiService.updateTask(task.id, {
        title: editTitle.trim(),
        description: editDescription.trim() || undefined,
      })) as Task;
      onTaskUpdated(updatedTask);
      setIsEditing(false);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = () => {
    setIsEditing(false);
    setEditTitle(task.title);
    setEditDescription(task.description || '');
  };

  const handleView = () => {
    setShowViewModal(true);
  };

  return (
    <div className="flex flex-col md:flex-row justify-between items-start p-4 bg-white border border-gray-200 rounded-lg shadow-sm mb-3 hover:shadow-lg transition-shadow duration-200">

      {/* Left: Checkbox + Title/Description */}
      <div className="flex items-start space-x-3 flex-1">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={handleToggle}
          disabled={loading}
          className="mt-1 w-5 h-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
        />

        {isEditing ? (
          <div className="flex-1 space-y-2 w-full">
            <input
              type="text"
              value={editTitle}
              onChange={(e) => setEditTitle(e.target.value)}
              className="w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 sm:text-sm px-3 py-2 transition-all duration-200"
              placeholder="Task title"
              disabled={loading}
            />
            <textarea
              value={editDescription}
              onChange={(e) => setEditDescription(e.target.value)}
              className="w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 sm:text-sm px-3 py-2 transition-all duration-200"
              placeholder="Task description"
              rows={2}
              disabled={loading}
            />
          </div>
        ) : (
          <div className="flex-1">
            <p
              className={`font-medium ${task.completed ? 'line-through text-gray-400' : 'text-gray-800'} cursor-pointer hover:underline`}
              onClick={handleView}
            >
              {task.title}
            </p>
            {task.description && (
              <p
                className="text-sm text-gray-600 cursor-pointer hover:underline mt-1"
                onClick={handleView}
              >
                {task.description}
              </p>
            )}
          </div>
        )}
      </div>

      {/* Right: Buttons */}
      <div className="flex space-x-2 mt-3 md:mt-0 ml-0 md:ml-4">
        {isEditing ? (
          <>
            <button
              onClick={handleSave}
              disabled={loading}
              className="px-3 py-1.5 bg-green-600 text-white text-sm font-medium rounded-md hover:bg-green-700 shadow transition-colors duration-200"
            >
              {loading ? 'Saving...' : 'Save'}
            </button>
            <button
              onClick={handleCancel}
              disabled={loading}
              className="px-3 py-1.5 bg-gray-200 text-gray-800 text-sm font-medium rounded-md hover:bg-gray-300 shadow transition-colors duration-200"
            >
              Cancel
            </button>
          </>
        ) : (
          <>
            <button
              onClick={handleView}
              disabled={loading}
              className="px-3 py-1.5 bg-indigo-100 text-indigo-700 text-sm font-medium rounded-md hover:bg-indigo-200 shadow transition-colors duration-200"
            >
              View
            </button>
            <button
              onClick={handleEdit}
              disabled={loading}
              className="px-5 py-1.5 bg-blue-100 text-blue-700 text-sm font-medium rounded-md hover:bg-blue-200 shadow transition-colors duration-200"
            >
              Edit
            </button>
            <button
              onClick={() => setShowDeleteModal(true)}
              disabled={loading}
              className="px-3 py-1.5 bg-red-100 text-red-700 text-sm font-medium rounded-md hover:bg-red-200 shadow transition-colors duration-200"
            >
              Delete
            </button>
          </>
        )}
      </div>

      {/* Delete Modal */}
      {showDeleteModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
          <div className="bg-white rounded-2xl shadow-2xl w-80 max-w-sm p-6 animate-fade-in scale-100 transition-transform">
            <h2 className="text-lg font-semibold mb-3 text-gray-800">Delete Task</h2>
            <p className="text-gray-600 mb-6 text-sm">
              Are you sure you want to delete this task? This action cannot be undone.
            </p>
            <div className="flex justify-end space-x-3">
              <button
                onClick={() => setShowDeleteModal(false)}
                className="px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium transition"
              >
                Cancel
              </button>
              <button
                onClick={handleDelete}
                disabled={loading}
                className="px-4 py-2 rounded-lg bg-red-600 hover:bg-red-700 text-white font-medium shadow transition"
              >
                {loading ? 'Deleting...' : 'Delete'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* View Task Modal */}
      {showViewModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
          <div className="bg-white rounded-2xl shadow-2xl w-96 max-w-md p-6 animate-fade-in scale-100 transition-transform">
            <h2 className="text-xl font-bold text-gray-900 mb-4">{task.title}</h2>
            <p className="text-gray-700 mb-4">{task.description || 'No description provided.'}</p>
            <p className={`text-sm font-medium ${task.completed ? 'text-green-600' : 'text-yellow-600'}`}>
              Status: {task.completed ? 'Completed' : 'Pending'}
            </p>
            <div className="mt-6 flex justify-end">
              <button
                onClick={() => setShowViewModal(false)}
                className="px-4 py-2 bg-blue-100 hover:bg-blue-200 text-blue-700 rounded-lg font-medium transition"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
