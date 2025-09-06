# Simple role-based access control (RBAC) implementation

ROLE_PERMISSIONS = {
    "admin": {"upload", "download", "delete", "view"},
    "user": {"upload", "download", "view"},
    "guest": {"view"},
}

def has_permission(role, action):
    """Check if the role is allowed to perform the given action."""
    return action in ROLE_PERMISSIONS.get(role, set())
