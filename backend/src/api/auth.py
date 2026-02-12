

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from datetime import timedelta
from ..database import get_session
from ..models.user import UserCreate
from ..schemas.user import UserLogin, Token
from ..services.user_service import UserService
from ..utils.auth import create_access_token
from ..utils.password import verify_password

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", response_model=Token)
def register(user_create: UserCreate, session: Session = Depends(get_session)):
    """Register a new user."""
    try:
        user = UserService.create_user(session, user_create)
        # Create access token
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during registration"
        )

@router.post("/login", response_model=Token)
def login(user_login: UserLogin, session: Session = Depends(get_session)):
    """Login an existing user."""
    user = UserService.authenticate_user(session, user_login.email, user_login.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
def logout():
    """Logout the current user (client-side token removal)."""
    # Since JWT tokens are stateless, we can't invalidate them on the server
    # The client should remove the token from local storage
    return {"message": "Successfully logged out"} 