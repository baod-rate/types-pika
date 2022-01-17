from __future__ import annotations

import abc
import re
from typing import Any
from typing import AnyStr
from typing import ItemsView
from typing import KeysView
from typing import Type
from typing import ValuesView

PY2: bool
PY3: bool
RE_NUM: re.Pattern

ON_LINUX: bool
ON_OSX: bool
ON_WINDOWS: bool

class AbstractBase(metaclass=abc.ABCMeta): ...

SOCKET_ERROR: Type[Exception]
SOL_TCP: int

basestring: tuple[Type[str]]
str_or_bytes: tuple[Type[str], Type[bytes]]
xrange: Type[range]
unicode_type: Type[str]


def time_now() -> float: ...
def dictkeys(dct) -> list[KeysView]: ...
def dictvalues(dct) -> list[ValuesView]: ...
def dict_iteritems(dct) -> ItemsView: ...
def dict_itervalues(dct) -> ValuesView: ...
def byte(*args: int) -> bytes: ...
class long(int):
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
def canonical_str(value) -> str: ...
def is_integer(value: Any) -> bool: ...

def as_bytes(value: AnyStr) -> bytes: ...
def to_digit(value): ...
def get_linux_version(release_str) -> tuple[int, int, int]: ...

HAVE_SIGNAL: bool
EINTR_IS_EXPOSED: bool
LINUX_VERSION: tuple[int, int, int] | None
_LOCALHOST: str
_LOCALHOST_V6: str
