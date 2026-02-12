import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend', 'src'))

# Change to the backend/src directory
os.chdir(os.path.join(os.path.dirname(__file__), 'backend', 'src'))

# Import and run the application
from main import app
import uvicorn

if __name__ == "__main__":
    try:
        print("Starting server...")
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    except Exception as e:
        print(f"Error starting server: {e}")
        import traceback
        traceback.print_exc()