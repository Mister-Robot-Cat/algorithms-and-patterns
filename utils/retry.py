"""Decorator for retrying operations with exponential backoff and jitter."""
import time
import random
import functools
import logging
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)

def retry_with_backoff(
    retries: int = 3,
    initial_delay: float = 0.5,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """Retry a function with exponential backoff upon specified exceptions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            delay = initial_delay
            last_err = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_err = e
                    if attempt == retries:
                        break
                    sleep_time = delay + random.uniform(0, 0.1 * delay)
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for {func.__name__}: {e}. Retrying in {sleep_time:.2f}s"
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor
            raise last_err
        return wrapper
    return decorator
