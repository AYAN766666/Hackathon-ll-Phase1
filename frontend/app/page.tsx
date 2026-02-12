'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import authService from '@/src/services/auth';

export default function HomePage() {
  const router = useRouter();

  useEffect(() => {
    const checkAuth = async () => {
      if (authService.isAuthenticated()) {
        // Check if token is still valid
        try {
          await authService.getUser();
          router.push('/dashboard');
        } catch (error) {
          // Token is invalid, redirect to login
          router.push('/login');
        }
      } else {
        router.push('/login');
      }
    };

    checkAuth();
  }, [router]);

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
        <p className="mt-4 text-gray-600">Redirecting...</p>
      </div>
    </div>
  );
}