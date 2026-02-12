
import React from 'react';
import { Task } from '@/src/services/api';

interface TaskDetailProps {
  task: Task | null;
  onClose: () => void;
}

export default function TaskDetail({ task, onClose }: TaskDetailProps) {
  // ✅ AGAR TASK HI NA HO TO KUCH RENDER NA KARO
  if (!task) return null;

  // Handle backdrop click to close the modal
  const handleBackdropClick = (e: React.MouseEvent<HTMLDivElement>) => {
    if (e.target === e.currentTarget) {
      onClose();
    }
  };

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-60 backdrop-blur-sm flex items-center justify-center p-4 z-50"
      onClick={handleBackdropClick}
    >
      <div
        className="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden transform transition-all"
        onClick={(e) => e.stopPropagation()} // modal ke andar click safe
      >
        {/* HEADER */}
        <div className="border-b border-gray-100 bg-gradient-to-r from-blue-50 to-indigo-50 p-6">
          <div className="flex justify-between items-start">
            <div className="flex-1 min-w-0">
              {/* ✅ TITLE SAFE */}
              <h2 className="text-2xl font-bold text-gray-900 break-words">
                {task.title || 'Untitled Task'}
              </h2>

              <div className="flex items-center mt-3 space-x-3">
                <span
                  className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium ${
                    task.completed
                      ? 'bg-green-100 text-green-800'
                      : 'bg-yellow-100 text-yellow-800'
                  }`}
                >
                  {task.completed ? 'Completed' : 'Pending'}
                </span>

                <span className="text-xs text-gray-500">
                  Created:{' '}
                  {task.created_at
                    ? new Date(task.created_at).toLocaleDateString()
                    : 'N/A'}
                </span>
              </div>
            </div>

            {/* ❌ BUTTON FIX */}
            <button
              onClick={onClose}
              type="button"
              className="text-gray-400 hover:text-gray-600 p-2 rounded-full hover:bg-gray-100 transition-colors duration-200"
              aria-label="Close"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        {/* BODY */}
        <div className="p-6">
          {task.description ? (
            <div className="bg-gradient-to-br from-blue-50 to-indigo-50 p-5 rounded-xl border border-blue-100 mb-6">
              <h3 className="text-sm font-semibold text-gray-700 mb-3 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                </svg>
                Description
              </h3>
              <p className="text-gray-700 whitespace-pre-wrap leading-relaxed">
                {task.description}
              </p>
            </div>
          ) : (
            <div className="bg-gray-50 p-5 rounded-xl border border-gray-100 mb-6 text-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 mx-auto text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              <p className="text-gray-500 mt-2">No description provided</p>
            </div>
          )}

          <div className="flex justify-end">
            <button
              onClick={onClose}
              type="button"
              className="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-lg hover:from-blue-700 hover:to-indigo-700 transition-all duration-200 shadow-md hover:shadow-lg font-medium"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
