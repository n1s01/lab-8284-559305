#!/usr/bin/env python3

"""Enum definitions for roles and actions used across the project.

The enums provide a type‑safe way to refer to roles and actions while
maintaining compatibility with existing string‑based usage.
"""

from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

    def __str__(self) -> str:
        return self.value

class Action(Enum):
    UPLOAD = "upload"
    DOWNLOAD = "download"
    DELETE = "delete"
    VIEW = "view"

    def __str__(self) -> str:
        return self.value

# Permissions mapping using enums (mirrors the previous ROLE_PERMISSIONS dict)
ROLE_PERMISSIONS = {
    Role.ADMIN: {Action.UPLOAD, Action.DOWNLOAD, Action.DELETE, Action.VIEW},
    Role.USER: {Action.UPLOAD, Action.DOWNLOAD, Action.VIEW},
    Role.GUEST: {Action.VIEW},
}
