
from sqlmodel import Session, select
from typing import Optional
from fastapi import HTTPException, status

from ..models.user import User, UserCreate
from ..utils.password import get_password_hash, verify_password


# 🔐 bcrypt hard limit
BCRYPT_MAX_BYTES = 72


def validate_password(password: str):
    if len(password.encode("utf-8")) > BCRYPT_MAX_BYTES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password is too long. Maximum allowed length is 72 bytes."
        )


class UserService:
    @staticmethod
    def create_user(session: Session, user_create: UserCreate) -> User:
        """Create a new user with hashed password."""

        # ✅ PASSWORD VALIDATION
        validate_password(user_create.password)

        # Check if user with email already exists
        existing_user = session.exec(
            select(User).where(User.email == user_create.email)
        ).first()

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Validate email format
        if "@" not in user_create.email or "." not in user_create.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format"
            )

        # Hash the password
        hashed_password = get_password_hash(user_create.password)

        # ✅ FIX: correct DB field name
        db_user = User(
            email=user_create.email,
            hashed_password=hashed_password   # 🔥 THIS WAS THE BUG
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user

    @staticmethod
    def authenticate_user(
        session: Session,
        email: str,
        password: str
    ) -> Optional[User]:

        validate_password(password)

        user = session.exec(
            select(User).where(User.email == email)
        ).first()

        if not user or not verify_password(password, user.hashed_password):
            return None

        return user

    @staticmethod
    def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
        return session.get(User, user_id)
