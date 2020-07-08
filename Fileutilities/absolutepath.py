from pathlib import Path


def abspath(filepath):
    relative = Path(filepath)
    return relative.absolute()