# circuit_breaker.py
from datetime import time
class CircuitBreaker:
    def __init__(self, max_failures, reset_timeout):
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.open = False

    def execute(self, func, *args, **kwargs):
        if self.open:
            return None

        try:
            result = func(*args, **kwargs)
            self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            if self.failure_count >= self.max_failures:
                self.open = True
                self.reset_timeout = time.time() + self.reset_timeout
            raise e

    def can_execute(self):
        if self.open and time.time() >= self.reset_timeout:
            self.open = False
            self.failure_count = 0
            return True
        return not self.open
