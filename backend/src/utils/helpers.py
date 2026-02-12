"""
Utility functions for the Todo Application AI Agent and MCP Server integration.
Contains common helper functions for UUID generation, timestamps, etc.
"""
from datetime import datetime
from uuid import UUID, uuid4
import time


def generate_uuid() -> UUID:
    """
    Generate a new UUID4.

    Returns:
        UUID: A new UUID4 instance
    """
    return uuid4()


def get_current_timestamp() -> datetime:
    """
    Get the current UTC timestamp.

    Returns:
        datetime: Current UTC datetime
    """
    return datetime.utcnow()


def get_current_timestamp_local() -> datetime:
    """
    Get the current local timestamp.

    Returns:
        datetime: Current local datetime
    """
    return datetime.now()


def uuid_to_str(uuid_val: UUID) -> str:
    """
    Convert a UUID to its string representation.

    Args:
        uuid_val: The UUID to convert

    Returns:
        str: String representation of the UUID
    """
    return str(uuid_val)


def str_to_uuid(uuid_str: str) -> UUID:
    """
    Convert a string to a UUID.

    Args:
        uuid_str: The string to convert

    Returns:
        UUID: UUID instance

    Raises:
        ValueError: If the string is not a valid UUID
    """
    return UUID(uuid_str)


def format_timestamp(timestamp: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format a timestamp according to the given format.

    Args:
        timestamp: The datetime to format
        fmt: The format string (default: "%Y-%m-%d %H:%M:%S")

    Returns:
        str: Formatted timestamp string
    """
    return timestamp.strftime(fmt)


def timestamp_to_iso(timestamp: datetime) -> str:
    """
    Convert a timestamp to ISO format string.

    Args:
        timestamp: The datetime to convert

    Returns:
        str: ISO format timestamp string
    """
    return timestamp.isoformat()


def sleep(seconds: float) -> None:
    """
    Sleep for the specified number of seconds.

    Args:
        seconds: Number of seconds to sleep
    """
    time.sleep(seconds)