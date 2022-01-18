from typing import Any, Sequence, TypeVar

from .descriptor import Descriptor, FieldDescriptor
from .internal.extension_dict import _ExtensionDict, _ExtensionFieldDescriptor

class Error(Exception): ...
class DecodeError(Error): ...
class EncodeError(Error): ...

_M = TypeVar("_M", bound=Message)  # message type (of self)

class Message:
    DESCRIPTOR: Descriptor
    def __deepcopy__(self, memo=...): ...
    def __eq__(self, other_msg): ...
    def __ne__(self, other_msg): ...
    def MergeFrom(self: _M, other_msg: _M) -> None: ...
    def CopyFrom(self: _M, other_msg: _M) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def ParseFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> Sequence[tuple[FieldDescriptor, Any]]: ...
    def HasExtension(self: _M, extension_handle: _ExtensionFieldDescriptor[_M, Any]) -> bool: ...
    def ClearExtension(self: _M, extension_handle: _ExtensionFieldDescriptor[_M, Any]) -> None: ...
    def ByteSize(self) -> int: ...
    @classmethod
    def FromString(cls: type[_M], s: bytes) -> _M: ...
    @property
    def Extensions(self: _M) -> _ExtensionDict[_M]: ...
    # Intentionally left out typing on these three methods, because they are
    # stringly typed and it is not useful to call them on a Message directly.
    # We prefer more specific typing on individual subclasses of Message
    # See https://github.com/dropbox/mypy-protobuf/issues/62 for details
    def HasField(self, field_name: Any) -> bool: ...
    def ClearField(self, field_name: Any) -> None: ...
    def WhichOneof(self, oneof_group: Any) -> Any: ...
    # TODO: check kwargs
    def __init__(self, **kwargs) -> None: ...
