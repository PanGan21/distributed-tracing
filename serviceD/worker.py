"""The Epsilon module."""

import time
import random
import logging

log = logging.getLogger(__name__)


class Worker(object):
    """The Worker class."""

    def __init__(self):
        log.info("Initializing the Worker object")

        self.data = {}
        self.data["fibonacci"] = None
        self.data["collatz"] = []

    def _fib(self, n):
        a, b = 0, 1
        log.debug("a is %d, b is %d", a, b)
        for _ in range(n):
            time.sleep(0.1)
            a, b = b, a + b
            log.debug("a is %d, b is %d", a, b)
        return a

    def _collatz(self, n):
        log.debug("n is %d", n)
        while True:
            time.sleep(0.1)
            if n == 1:
                log.debug("n is %d", n)
                break
            if n % 2 == 0:
                n = n // 2
                log.debug("n is %d", n)
                yield n
            else:
                n = n * 3 + 1
                log.debug("n is %d", n)
                yield n
        yield n

    def compute(self):
        """Perform some computation."""
        log.info("Started computing ...")

        seed = random.randint(10, 19)
        log.info("The seed is %d", seed)

        fib = self._fib(seed)
        log.info("The %d-th Fibonacci number is %d", seed, fib)
        self.data["fibonacci"] = fib

        for c in self._collatz(fib):
            self.data["collatz"].append(c)
