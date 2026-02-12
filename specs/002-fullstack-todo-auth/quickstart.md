# Quickstart Guide: Full-Stack Todo Application

## Prerequisites

- Node.js 18+ with npm/yarn
- Python 3.13+
- uv (Python package manager)
- A SQL database (SQLite for development, PostgreSQL for production)

## Setup Instructions

### 1. Clone and Initialize Repository

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install Python dependencies with uv
cd backend
uv init
uv add fastapi sqlmodel python-jose bcrypt python-multipart python-dotenv
uv sync
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env with your database URL and secret keys

# Run database migrations (if applicable)
uv run python -m src.main migrate

# Start the backend server
uv run python -m src.main dev
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
# Edit with your backend API URL

# Start the development server
npm run dev
```

## API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout

### Users
- `GET /users/me` - Get current user info

### Tasks
- `GET /tasks` - Get user's tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task
- `PATCH /tasks/{id}/complete` - Toggle task completion

## Environment Variables

### Backend (.env)
```env
DATABASE_URL=sqlite:///./todo_app.db
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Running Tests

### Backend Tests
```bash
cd backend
uv run pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Development Workflow

1. Start the backend server
2. Start the frontend development server
3. Access the application at `http://localhost:3000`
4. Register a new account or login with existing credentials
5. Create and manage tasks through the dashboard

## Database Migrations

If using PostgreSQL or other SQL databases:
```bash
# Run migrations
uv run alembic upgrade head

# Create new migration
uv run alembic revision --autogenerate -m "migration message"
```