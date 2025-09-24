#!/usr/bin/env python3

"""File I/O helper functions using context managers.

Provides simple read and write operations that automatically manage file
resources via the ``with`` statement.
"""

def read_file(path: str, encoding: str = "utf-8") -> str:
    """Read the entire contents of *path* and return as a string.

    The function opens the file in text mode using the specified *encoding*
    and ensures the file is closed when the operation completes.
    """
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def write_file(path: str, data: str, encoding: str = "utf-8") -> None:
    """Write *data* to *path*, overwriting any existing content.

    The file is opened in text write mode with the given *encoding* and is
    automatically closed after writing.
    """
    with open(path, "w", encoding=encoding) as f:
        f.write(data)
