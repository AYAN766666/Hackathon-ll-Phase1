'use client';

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import authService from '@/src/services/auth';

interface User {
  id: number;
  email: string;
  created_at: string;
}

interface UserContextType {
  user: User | null;
  loading: boolean;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  signup: (email: string, password: string) => Promise<void>;
  logout: () => void;
  fetchUser: () => Promise<void>;
}

const UserContext = createContext<UserContextType | undefined>(undefined);

export function UserProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      if (authService.isAuthenticated()) {
        try {
          const userData = await authService.getUser();
          setUser(userData);
        } catch (error) {
          console.error('Failed to fetch user:', error);
          authService.logout(); // Clear invalid token
        }
      }
      setLoading(false);
    };

    initAuth();
  }, []);

  const login = async (email: string, password: string) => {
    const tokenData = await authService.login({ email, password });
    const userData = await authService.getUser();
    setUser(userData);
  };

  const signup = async (email: string, password: string) => {
    const tokenData = await authService.signup({ email, password });
    const userData = await authService.getUser();
    setUser(userData);
  };

  const logout = () => {
    authService.logout();
    setUser(null);
  };

  const fetchUser = async () => {
    if (authService.isAuthenticated()) {
      try {
        const userData = await authService.getUser();
        setUser(userData);
      } catch (error) {
        console.error('Failed to fetch user:', error);
        authService.logout();
        setUser(null);
      }
    }
  };

  const value: UserContextType = {
    user,
    loading,
    isAuthenticated: !!user,
    login,
    signup,
    logout,
    fetchUser,
  };

  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
}

export function useUser() {
  const context = useContext(UserContext);
  if (context === undefined) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
}