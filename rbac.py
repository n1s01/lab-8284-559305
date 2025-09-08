# Simple role-based access control (RBAC) implementation

from constants import ROLE_PERMISSIONS

def has_permission(role, action):
    """Check if the role is allowed to perform the given action."""
    return action in ROLE_PERMISSIONS.get(role, set())
