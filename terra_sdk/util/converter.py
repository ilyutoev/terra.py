from datetime import datetime
from typing import Dict, Any
import json
from .remove_none import remove_none

__all__ = ['to_isoformat', 'bytes_to_dict']


def to_isoformat(dt: datetime) -> str:
    return (
        dt.isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
        .replace("000Z", "Z")
    )


def bytes_to_dict(obj: bytes) -> Dict[str, Any]:
    res = json.loads(obj.decode())
    return remove_none(res)
