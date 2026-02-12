
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface AiAgentResponse {
  response: string;
  action_performed: boolean;
  action_result?: {
    task_id?: number;
    task_title?: string;
    task_count?: number;
  };
}

/**
 * Send a message to the AI agent
 */
export const sendAiAgentMessage = async (
  message: string
): Promise<AiAgentResponse> => {
  try {
    // ✅ Get token
    const token = localStorage.getItem('access_token');
    if (!token) throw new Error('No authentication token found');

    // ✅ Decode JWT to get user_id
    const decoded: any = jwtDecode(token);
    const user_id = decoded.sub;
    if (!user_id) {
      console.error('JWT token payload:', decoded);
      throw new Error('No user_id found in token. Invalid token format.');
    }

    // ✅ POST request - send the message in a JSON object
    const response = await axios.post(
      `${API_BASE_URL}/ai-agent/message`,
      { message }, // Send message in a JSON object
      {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      }
    );

    return response.data as AiAgentResponse;
  } catch (error: any) {
    console.error('Error sending message to AI agent:', error);

    if (axios.isAxiosError(error)) {
      const status = error.response?.status;
      const detail =
        error.response?.data?.detail || JSON.stringify(error.response?.data);

      if (status === 401) throw new Error('Unauthorized: Please log in again');
      if (status === 422) throw new Error('Invalid request: ' + detail);
      if (status)
        throw new Error(`Server error (${status}): ${detail}`);
    }

    throw new Error(
      'Failed to communicate with AI agent: ' +
        (error.message || error)
    );
  }
};

/**
 * Health check
 */
export const checkAiAgentHealth = async (): Promise<boolean> => {
  try {
    const response = await axios.get(
      `${API_BASE_URL}/ai-agent/health`
    );
    return response.data?.status === 'healthy';
  } catch (error) {
    console.error('AI agent health check failed:', error);
    return false;
  }
};
