#!/usr/bin/env python3

"""Simple Dependency Injection (DI) container.

Provides a Container class that supports registering factories or instances with
singleton or transient lifetimes and resolving them by key.

Example usage:
    from di_container import Container
    container = Container()
    container.register('logger', lambda: logging.getLogger('app'))
    logger = container.resolve('logger')
"""

from typing import Any, Callable, Dict

class _Provider:
    def __init__(self, factory: Callable[[], Any], singleton: bool):
        self._factory = factory
        self._singleton = singleton
        self._instance = None

    def get(self) -> Any:
        if self._singleton:
            if self._instance is None:
                self._instance = self._factory()
            return self._instance
        return self._factory()


class Container:
    """A minimal DI container.

    Register services with a unique key. By default services are treated as
    singletons; set `singleton=False` for transient (new instance each resolve).
    """

    def __init__(self) -> None:
        self._providers: Dict[str, _Provider] = {}

    def register(self, key: str, factory: Callable[[], Any], singleton: bool = True) -> None:
        """Register a factory for `key`.

        Args:
            key: Unique identifier for the service.
            factory: Callable that returns an instance of the service.
            singleton: If True, the same instance is returned on each resolve.
        """
        if key in self._providers:
            raise KeyError(f"Service '{key}' is already registered.")
        self._providers[key] = _Provider(factory, singleton)

    def resolve(self, key: str) -> Any:
        """Resolve and return the service associated with `key`."""
        provider = self._providers.get(key)
        if provider is None:
            raise KeyError(f"Service '{key}' is not registered.")
        return provider.get()

    def replace(self, key: str, factory: Callable[[], Any], singleton: bool = True) -> None:
        """Replace an existing registration with a new factory.

        Useful for testing or reconfiguration.
        """
        self._providers[key] = _Provider(factory, singleton)

    def clear(self) -> None:
        """Remove all registered services."""
        self._providers.clear()
