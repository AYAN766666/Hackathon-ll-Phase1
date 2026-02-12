import os
import sys

# Change to the backend/src directory
backend_src_dir = os.path.join(os.path.dirname(__file__), 'backend', 'src')
os.chdir(backend_src_dir)
sys.path.insert(0, backend_src_dir)

# Add the parent directory to the path as well
parent_dir = os.path.dirname(backend_src_dir)
sys.path.insert(0, parent_dir)

# Now run the server
try:
    import uvicorn
    import main
    print("Starting server on http://127.0.0.1:8000")
    uvicorn.run(main.app, host="127.0.0.1", port=8000, log_level="info", reload=False)
except Exception as e:
    print(f"Error starting server: {e}")
    import traceback
    traceback.print_exc()