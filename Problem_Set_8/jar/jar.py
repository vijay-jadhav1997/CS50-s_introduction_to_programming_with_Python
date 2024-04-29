class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{'🍪' * self._size}"

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError(
                "Deposit value can't be negative integer.")
        if self._size + n > self._capacity:
            raise ValueError("Adding cookies would exceed the capacity of jar.")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError(
                "Number of cookies to withdraw must be a non-negative integer.")
        if n > self._size:
            raise ValueError("Insufficient cookies in the jar, can't withdraw.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
