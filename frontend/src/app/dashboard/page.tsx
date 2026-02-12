
'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import authService from '@/src/services/auth';
import apiService from '@/src/services/api';
import TaskList from '@/src/components/TaskList';
import TaskForm from '@/src/components/TaskForm';
import Navbar from '@/src/components/Navbar';
import ProtectedRoute from '@/src/components/ProtectedRoute';

export default function DashboardPage() {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [tasks, setTasks] = useState<any[]>([]);
  const [showTaskForm, setShowTaskForm] = useState(false);
  const router = useRouter();

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const userData = await authService.getUser();
        setUser(userData);

        const tasksData = await apiService.getTasks();
        setTasks(tasksData);
      } catch (error) {
        console.error('Error fetching user data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchUserData();
  }, [router]);

  // ✅ FIXED
  const handleTaskCreated = (newTask: any) => {
    setTasks(prev => [newTask, ...prev]);
    setShowTaskForm(false);
  };

  // ✅ SAFE UPDATE
  const handleTaskUpdated = (updatedTask: any) => {
    setTasks(prev =>
      prev.map(task =>
        task.id === updatedTask.id ? updatedTask : task
      )
    );
  };

  // ✅ SAFE DELETE
  const handleTaskDeleted = (taskId: number) => {
    setTasks(prev => prev.filter(task => task.id !== taskId));
  };

  // ✅ SAFE TOGGLE
  const handleTaskToggled = async (taskId: number, completed: boolean) => {
    try {
      const updatedTask = await apiService.toggleTaskCompletion(taskId, completed);
      setTasks(prev =>
        prev.map(task =>
          task.id === taskId ? updatedTask : task
        )
      );
    } catch (error) {
      console.error('Error toggling task:', error);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-blue-600 mx-auto animate-pulse"></div>
          <p className="mt-4 text-gray-600 text-lg font-medium">Loading your dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
        <Navbar />

        <div className="max-w-6xl mx-auto py-8 px-4 animate-fade-in">
          <div className="flex justify-between items-center mb-8">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
              <p className="text-gray-600 mt-1">Manage your tasks efficiently</p>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="bg-white/80 backdrop-blur-sm rounded-xl p-4 border border-white/30 shadow-sm">
                <p className="text-sm text-gray-600">Total Tasks</p>
                <p className="text-2xl font-bold text-blue-600">{tasks.length}</p>
              </div>
              
              <button
                onClick={() => setShowTaskForm(!showTaskForm)}
                className="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl hover:from-blue-700 hover:to-purple-700 transition-all duration-300 transform hover:scale-105 hover-lift shadow-lg flex items-center"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                {showTaskForm ? 'Cancel' : 'New Task'}
              </button>
            </div>
          </div>

          {showTaskForm && (
            <div className="mb-8 animate-fade-in">
              <div className="bg-white/80 backdrop-blur-sm rounded-2xl p-6 border border-white/30 shadow-lg">
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Create New Task</h3>
                <TaskForm onTaskCreated={handleTaskCreated} />
              </div>
            </div>
          )}

          <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl border border-white/30 overflow-hidden">
            <div className="px-6 py-5 border-b border-gray-200/50">
              <h2 className="text-xl font-semibold text-gray-800 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
                Your Tasks ({tasks.length})
              </h2>
            </div>
            
            <div className="p-4">
              <TaskList
                tasks={tasks}
                onTaskUpdated={handleTaskUpdated}
                onTaskDeleted={handleTaskDeleted}
                onTaskToggled={handleTaskToggled}
              />
            </div>
          </div>
          
          {tasks.length === 0 && (
            <div className="mt-12 text-center animate-fade-in">
              <div className="mx-auto w-24 h-24 bg-gradient-to-r from-blue-100 to-purple-100 rounded-full flex items-center justify-center mb-6">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">No tasks yet</h3>
              <p className="text-gray-600 max-w-md mx-auto mb-6">
                Get started by creating your first task. Organize your work and boost your productivity.
              </p>
              <button
                onClick={() => setShowTaskForm(true)}
                className="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl hover:from-blue-700 hover:to-purple-700 transition-all duration-300 transform hover:scale-105 hover-lift shadow-lg"
              >
                Create Your First Task
              </button>
            </div>
          )}
        </div>
      </div>
    </ProtectedRoute>
  );
}
