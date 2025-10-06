# Simple role-based access control (RBAC) implementation

from enums import Role, Action, ROLE_PERMISSIONS

def _normalize_role(role):
    """Convert role to Role enum if needed."""
    if isinstance(role, Role):
        return role
    # Accept string representation
    try:
        return Role(role)
    except ValueError:
        raise ValueError(f"Unknown role: {role}")

def _normalize_action(action):
    """Convert action to Action enum if needed."""
    if isinstance(action, Action):
        return action
    # Accept string representation
    try:
        return Action(action)
    except ValueError:
        raise ValueError(f"Unknown action: {action}")

def has_permission(role, action):
    """Check if the role is allowed to perform the given action.

    Parameters can be either enum members or their string values.
    """
    role_enum = _normalize_role(role)
    action_enum = _normalize_action(action)
    return action_enum in ROLE_PERMISSIONS.get(role_enum, set())
