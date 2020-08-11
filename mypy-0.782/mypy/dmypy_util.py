"""Shared code between dmypy.py and dmypy_server.py.

This should be pretty lightweight and not depend on other mypy code (other than ipc).
"""

import json

from typing import Any
from typing_extensions import Final

from mypy.ipc import IPCBase

DEFAULT_STATUS_FILE = '.dmypy.json'  # type: Final


def receive(connection: IPCBase) -> Any:
    """Receive JSON data from a connection until EOF.

    Raise OSError if the data received is not valid JSON or if it is
    not a dict.
    """
    bdata = connection.read()
    if not bdata:
        raise OSError("No data received")
    try:
        data = json.loads(bdata.decode('utf8'))
    except Exception:
        raise OSError("Data received is not valid JSON")
    if not isinstance(data, dict):
        raise OSError("Data received is not a dict (%s)" % str(type(data)))
    return data
