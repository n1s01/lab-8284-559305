#!/usr/bin/env python3

"""Repository pattern implementation.

Provides a generic Repository base class for CRUD operations on an in-memory
store, and an example UserRepository.
"""

class Repository:
    """A simple in-memory repository."""
    def __init__(self):
        self._store = {}

    def add(self, key, value):
        self._store[key] = value

    def get(self, key):
        return self._store.get(key)

    def delete(self, key):
        if key in self._store:
            del self._store[key]

    def list(self):
        return list(self._store.values())

class UserRepository(Repository):
    """Repository for user entities."""
    def find_by_username(self, username):
        return next((u for u in self._store.values() if getattr(u, "username", None) == username), None)
