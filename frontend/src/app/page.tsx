'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import authService from '@/src/services/auth';

export default function HomePage() {
  const router = useRouter();
  const [isLoading, setIsLoading] = useState(true);

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
        setIsLoading(false); // Show the landing page if not authenticated
      }
    };

    checkAuth();
  }, [router]);

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-blue-600 mx-auto animate-pulse"></div>
          <p className="mt-4 text-gray-600 text-lg font-medium">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
      {/* Hero Section */}
      <div className="relative overflow-hidden">
        <div className="max-w-7xl mx-auto">
          <div className="relative z-10 pb-8 sm:pb-16 md:pb-20 lg:max-w-2xl lg:w-full lg:pb-28 xl:pb-32">
            <main className="mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
              <div className="sm:text-center lg:text-left">
                <h1 className="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
                  <span className="block animate-fade-in">Welcome to</span>
                  <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 animate-fade-in-delay">
                    Smart Todo App
                  </span>
                </h1>
                <p className="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0 animate-fade-in-delay">
                  A powerful and intuitive task management application that helps you stay organized and productive. 
                  Manage your tasks, set priorities, and achieve your goals with our smart AI-powered assistant.
                </p>
                <div className="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start space-x-4">
                  <div className="rounded-md shadow">
                    <Link
                      href="/signup"
                      className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 md:py-4 md:text-lg md:px-10 transition-all duration-300 transform hover:scale-105 hover-lift"
                    >
                      Get started
                    </Link>
                  </div>
                  <div className="mt-3 sm:mt-0">
                    <Link
                      href="/login"
                      className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-blue-700 bg-blue-100 hover:bg-blue-200 md:py-4 md:text-lg md:px-10 transition-all duration-300 transform hover:scale-105 hover-lift"
                    >
                      Sign in
                    </Link>
                  </div>
                </div>
              </div>
            </main>
          </div>
        </div>
        <div className="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
          <div className="h-56 w-full bg-gradient-to-r from-blue-400 to-purple-500 sm:h-72 md:h-96 lg:w-full lg:h-full flex items-center justify-center">
            <div className="relative w-4/5 h-4/5 bg-white/20 backdrop-blur-sm rounded-2xl border border-white/30 flex items-center justify-center">
              <div className="text-white text-center p-6">
                <div className="text-5xl mb-4 animate-bounce">📋</div>
                <h3 className="text-xl font-bold">Smart Task Management</h3>
                <p className="mt-2">Organize your life with AI assistance</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="py-12 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-base font-semibold text-blue-600 tracking-wide uppercase">Features</h2>
            <p className="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
              Everything you need to stay organized
            </p>
            <p className="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
              Our platform offers powerful tools to help you manage your tasks efficiently.
            </p>
          </div>

          <div className="mt-10">
            <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {[
                {
                  title: 'AI-Powered Assistant',
                  description: 'Get intelligent suggestions and automate routine tasks with our AI assistant.',
                  icon: '🤖',
                },
                {
                  title: 'Real-time Sync',
                  description: 'Access your tasks from anywhere with seamless synchronization across devices.',
                  icon: '🔄',
                },
                {
                  title: 'Priority Management',
                  description: 'Set priorities and deadlines to focus on what matters most.',
                  icon: '⚡',
                },
                {
                  title: 'Secure Authentication',
                  description: 'Enterprise-grade security to keep your data safe and private.',
                  icon: '🔒',
                },
                {
                  title: 'Intuitive Interface',
                  description: 'Clean and modern design that makes task management effortless.',
                  icon: '✨',
                },
                {
                  title: 'Progress Tracking',
                  description: 'Visualize your productivity and track your achievements over time.',
                  icon: '📊',
                },
              ].map((feature, index) => (
                <div 
                  key={index} 
                  className={`pt-6 animate-fade-in-delay ${index > 0 ? `delay-${index * 100}ms` : ''}`} 
                  style={{ animationDelay: `${index * 100}ms` }}
                >
                  <div className="flow-root bg-gray-50 rounded-lg px-6 pb-8 hover-lift transition-all duration-300">
                    <div className="-mt-6">
                      <div>
                        <div className="inline-flex items-center justify-center p-3 bg-gradient-to-r from-blue-500 to-purple-500 rounded-md shadow-lg">
                          <span className="text-2xl">{feature.icon}</span>
                        </div>
                      </div>
                      <h3 className="mt-8 text-lg font-medium text-gray-900 tracking-tight">{feature.title}</h3>
                      <p className="mt-5 text-base text-gray-500">
                        {feature.description}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600">
        <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-16 lg:px-8 lg:flex lg:items-center lg:justify-between">
          <h2 className="text-3xl font-extrabold tracking-tight text-white sm:text-4xl">
            <span className="block">Ready to start organizing?</span>
            <span className="block text-blue-200">Join thousands of productive users today.</span>
          </h2>
          <div className="mt-8 flex lg:mt-0 lg:flex-shrink-0">
            <div className="inline-flex rounded-md shadow">
              <Link
                href="/signup"
                className="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-blue-600 bg-white hover:bg-blue-50 transition-all duration-300 transform hover:scale-105"
              >
                Get started
              </Link>
            </div>
            <div className="ml-3 inline-flex rounded-md shadow">
              <Link
                href="/login"
                className="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-500 bg-opacity-60 hover:bg-opacity-70 transition-all duration-300"
              >
                Sign in
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}