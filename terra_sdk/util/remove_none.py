from boltons.iterutils import remap  # type: ignore
from typing import Any, Dict
__all__ = ["remove_none"]


def remove_none(obj: Dict[str, Any]) -> Dict[str, Any]:
    """remove keys for None in a dict"""
    return remap(
        obj, visit=lambda path, key, value: key is not None and value is not None
    )
