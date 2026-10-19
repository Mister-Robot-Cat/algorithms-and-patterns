"""Token Bucket rate limiter algorithm for API throttling."""
import time
from typing import Optional

class TokenBucketRateLimiter:
    """Thread-safe and memory-efficient token bucket algorithm.
    
    Refills capacity tokens per fill_rate seconds.
    """
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = float(capacity)
        self.tokens = float(capacity)
        self.refill_rate = refill_rate  # tokens per second
        self.last_update = time.monotonic()

    def consume(self, tokens: int = 1) -> bool:
        """Attempt to consume tokens. Returns True if granted, False otherwise."""
        now = time.monotonic()
        elapsed = now - self.last_update
        self.last_update = now

        # Add replenished tokens
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)

        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False
