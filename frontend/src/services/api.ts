
// API base URL
const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// ================= TYPES =================

export interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  user_id: number;
  created_at: string;
}

export interface CreateTaskData {
  title: string;
  description?: string;
  completed?: boolean;
}

export interface UpdateTaskData {
  title?: string;
  description?: string;
  completed?: boolean;
}

// ================= API SERVICE =================

class ApiService {
  private getToken(): string | null {
    if (typeof window === 'undefined') return null;
    return localStorage.getItem('access_token');
  }

  // ✅ SAFE RESPONSE HANDLER (GET / POST / PUT)
  private async handleResponse<T>(
    response: Response,
    fallbackError: string
  ): Promise<T | null> {
    let data: any = null;

    try {
      const contentType = response.headers.get('content-type');
      if (contentType?.includes('application/json')) {
        data = await response.json();
      }
    } catch {
      data = null;
    }

    if (!response.ok) {
      console.warn('API ERROR:', {
        status: response.status,
        message: data?.detail || fallbackError,
      });
      return null;
    }

    return data as T;
  }

  // ================= TASKS =================

  async getTasks(): Promise<Task[]> {
    const token = this.getToken();
    if (!token) return [];

    const response = await fetch(`${API_BASE_URL}/tasks/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await this.handleResponse<Task[]>(
      response,
      'Failed to fetch tasks'
    );

    return data ?? [];
  }

  async createTask(taskData: CreateTaskData): Promise<Task | null> {
    const token = this.getToken();
    if (!token || !taskData.title?.trim()) return null;

    const response = await fetch(`${API_BASE_URL}/tasks/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(taskData),
    });

    return this.handleResponse<Task>(
      response,
      'Failed to create task'
    );
  }

  async updateTask(
    taskId: number,
    taskData: UpdateTaskData
  ): Promise<Task | null> {
    const token = this.getToken();
    if (!token) return null;

    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(taskData),
    });

    return this.handleResponse<Task>(
      response,
      'Failed to update task'
    );
  }

  // ✅ ✅ ✅ DELETE — REAL FIX HERE
  async deleteTask(taskId: number): Promise<boolean> {
    const token = this.getToken();
    if (!token) return false;

    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
      method: 'DELETE',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      console.warn('Delete failed:', response.status);
      return false;
    }

    // ✅ DELETE SUCCESS (no JSON needed)
    return true;
  }

  async toggleTaskCompletion(
    taskId: number,
    completed: boolean
  ): Promise<Task | null> {
    const token = this.getToken();
    if (!token) return null;

    const response = await fetch(
      `${API_BASE_URL}/tasks/${taskId}/complete?completed=${completed}`,
      {
        method: 'PATCH',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    return this.handleResponse<Task>(
      response,
      'Failed to toggle task completion'
    );
  }
}

const apiService = new ApiService();
export default apiService;
