#!/usr/bin/env python3

import subprocess
from datetime import datetime

def generate_changelog(output_path="CHANGELOG.md"):
    """Generate a simple changelog from git commit messages."""
    try:
        result = subprocess.run(
            ["git", "log", "--pretty=format:* %s"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        lines = result.stdout.splitlines()
        header = f"# Changelog\n\nGenerated on {datetime.utcnow().isoformat()} UTC\n\n"
        content = header + "\n".join(lines) + "\n"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        raise RuntimeError(f"Failed to generate changelog: {e}")

if __name__ == "__main__":
    generate_changelog()
