
'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import authService, { User } from '@/src/services/auth';

export default function Navbar() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [isLoggingOut, setIsLoggingOut] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [showLogoutModal, setShowLogoutModal] = useState(false);

  // Fetch user on mount
  useEffect(() => {
    const fetchUser = async () => {
      try {
        const currentUser = await authService.getUser();
        setUser(currentUser);
      } catch (err) {
        console.error('Error fetching user:', err);
      } finally {
        setIsLoading(false);
      }
    };
    fetchUser();
  }, []);

  const confirmLogout = async () => {
    setIsLoggingOut(true);
    try {
      await authService.logout();
      setUser(null);
      setShowLogoutModal(false);
      router.replace('/login');
    } catch (error) {
      console.error('Logout failed:', error);
    } finally {
      setIsLoggingOut(false);
    }
  };

  return (
    <nav className="bg-gradient-to-r from-blue-600 to-indigo-700 shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">

          {/* LOGO */}
          <div className="flex items-center">
            <div className="bg-white rounded-lg p-1.5 mr-3">
              <svg
                className="h-6 w-6 text-indigo-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2"
                />
              </svg>
            </div>
            <h1 className="text-xl font-bold text-white">Todo App</h1>
          </div>

          {/* USER EMAIL + LOGOUT BUTTON */}
          <div className="flex items-center space-x-4">
            {/* Show email if available */}
            {!isLoading && user && (
              <div className="flex items-center bg-blue-500/30 rounded-full px-3 py-1.5">
                <span className="text-sm text-white truncate max-w-xs">{user.email}</span>
              </div>
            )}

            {/* Logout button always visible */}
            <button
              onClick={() => setShowLogoutModal(true)}
              disabled={isLoggingOut}
              className={`px-4 py-2 rounded-lg text-white font-medium bg-red-600 hover:bg-red-700 shadow-lg transition ${
                isLoggingOut ? 'opacity-70 cursor-not-allowed' : ''
              }`}
            >
              {isLoggingOut ? 'Logging out...' : 'Logout'}
            </button>
          </div>
        </div>
      </div>

      {/* Logout Modal */}
      {showLogoutModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 w-80 shadow-lg">
            <h2 className="text-lg font-semibold mb-4 text-gray-800">Confirm Logout</h2>
            <p className="mb-6 text-gray-600">Are you sure you want to logout?</p>
            <div className="flex justify-end space-x-3">
              <button
                onClick={() => setShowLogoutModal(false)}
                className="px-4 py-2 rounded-lg bg-gray-300 hover:bg-gray-400 text-gray-800 font-medium transition"
              >
                Cancel
              </button>
              <button
                onClick={confirmLogout}
                className="px-4 py-2 rounded-lg bg-red-600 hover:bg-red-700 text-white font-medium shadow transition"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      )}
    </nav>
  );
}
