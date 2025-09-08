# constants.py

# Maximum upload size (5 MB)
MAX_UPLOAD_SIZE = 5 * 1024 * 1024

# Allowed file extensions for uploads
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.pdf'}

# Role-based access control permissions
ROLE_PERMISSIONS = {
    "admin": {"upload", "download", "delete", "view"},
    "user": {"upload", "download", "view"},
    "guest": {"view"},
}
