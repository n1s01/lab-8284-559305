#!/usr/bin/env python3

import logging

logger = logging.getLogger('audit')

class Transaction:
    """Simple transaction context manager for audit logging."""
    def __init__(self, name="default"):
        self.name = name

    def __enter__(self):
        logger.info(f"Transaction {self.name} started")
        # Initialize transaction resources here
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            logger.error(f"Transaction {self.name} failed: {exc}")
            # Rollback logic could be placed here
        else:
            logger.info(f"Transaction {self.name} completed")
        # Do not suppress exceptions
        return False
