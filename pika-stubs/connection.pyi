from __future__ import annotations

import numbers
import ssl
from typing import Any, Callable, Dict, Mapping, Optional, Union

from typing_extensions import Literal

from . import (
    callback,
    channel as channel_,
    compat,
    credentials as credentials_,
    frame,
    spec,
)

PRODUCT: str

_OnHeartbeatTimeoutCallback = Callable[['Connection', numbers.Integral], int]
_OnCloseCallback = Callable[['Connection', Exception], None]
_OnConnectionBlockedCallback = Callable[
    [
        'Connection',
        frame.Method[spec.Connection.Blocked]
    ],
    None,
]
_OnConnectionUnblockedCallback = Callable[
    [
        'Connection',
        frame.Method[spec.Connection.Unblocked],
    ],
    None,
]
_OnOpenCallback = Callable[['Connection'], None]
_OnOpenErrorCallback = Callable[['Connection', Union[str, Exception]], None]
_OnOpenChannelCallback = Callable[[channel_.Channel], None]


class Parameters:

    DEFAULT_USERNAME: str = ...
    DEFAULT_PASSWORD: str = ...

    DEFAULT_BLOCKED_CONNECTION_TIMEOUT: Optional[numbers.Real] = ...
    DEFAULT_CHANNEL_MAX: int = ...
    DEFAULT_CLIENT_PROPERTIES: Optional[Mapping[str, Any]] = ...
    DEFAULT_CREDENTIALS: credentials_.VALID_TYPES = ...
    DEFAULT_CONNECTION_ATTEMPTS: Literal[1] = ...
    DEFAULT_FRAME_MAX: int = ...
    DEFAULT_HEARTBEAT_TIMEOUT: Optional[Union[numbers.Integral, _OnHeartbeatTimeoutCallback]] = ...
    DEFAULT_HOST: str = ...
    DEFAULT_LOCALE: str = ...
    DEFAULT_PORT: int = ...
    DEFAULT_RETRY_DELAY: numbers.Real = ...
    DEFAULT_SOCKET_TIMEOUT: numbers.Real = ...
    DEFAULT_STACK_TIMEOUT: numbers.Real = ...
    DEFAULT_SSL: bool = ...
    DEFAULT_SSL_OPTIONS: Optional[SSLOptions] = ...
    DEFAULT_SSL_PORT: int = ...
    DEFAULT_VIRTUAL_HOST: str = ...
    DEFAULT_TCP_OPTIONS: Optional[Mapping[str, Any]] = ...

    @property
    def blocked_connection_timeout(self) -> numbers.Real: ...
    @blocked_connection_timeout.setter
    def blocked_connection_timeout(self, value: Optional[numbers.Real]) -> None: ...
    @property
    def channel_max(self) -> numbers.Integral: ...
    @channel_max.setter
    def channel_max(self, value: numbers.Integral) -> None: ...
    @property
    def client_properties(self) -> Optional[Mapping[str, Any]]: ...
    @client_properties.setter
    def client_properties(self, value: Optional[Mapping[str, Any]]) -> None: ...
    @property
    def connection_attempts(self) -> numbers.Integral: ...
    @connection_attempts.setter
    def connection_attempts(self, value: numbers.Integral) -> None: ...
    @property
    def credentials(self) -> credentials_.VALID_TYPES: ...
    @credentials.setter
    def credentials(self, value: credentials_.VALID_TYPES) -> None: ...
    @property
    def frame_max(self) -> numbers.Integral: ...
    @frame_max.setter
    def frame_max(self, value: numbers.Integral) -> None: ...
    @property
    def heartbeat(self) -> Optional[Union[numbers.Integral, _OnHeartbeatTimeoutCallback]]: ...

    @heartbeat.setter
    def heartbeat(
        self,
        value: Optional[Union[numbers.Integral, _OnHeartbeatTimeoutCallback]],
    ) -> None: ...

    @property
    def host(self) -> str: ...
    @host.setter
    def host(self, value: str) -> None: ...
    @property
    def locale(self) -> str: ...
    @locale.setter
    def locale(self, value: str) -> str: ...
    @property
    def port(self) -> int: ...
    @port.setter
    def port(self, value: int) -> None: ...
    @property
    def retry_delay(self) -> numbers.Real: ...
    @retry_delay.setter
    def retry_delay(self, value: numbers.Real) -> None: ...
    @property
    def socket_timeout(self) -> Optional[numbers.Real]: ...
    @socket_timeout.setter
    def socket_timeout(self, value: Optional[numbers.Real]) -> None: ...
    @property
    def stack_timeout(self) -> Optional[numbers.Real]: ...
    @stack_timeout.setter
    def stack_timeout(self, value: Optional[numbers.Real]) -> None: ...
    @property
    def ssl_options(self) -> Optional[SSLOptions]: ...
    @ssl_options.setter
    def ssl_options(self, value: Optional[SSLOptions]) -> None: ...
    @property
    def virtual_host(self) -> str: ...
    @virtual_host.setter
    def virtual_host(self, value: str) -> None: ...
    @property
    def tcp_options(self) -> Optional[Mapping[str, Any]]: ...
    @tcp_options.setter
    def tcp_options(self, value: Optional[Mapping[str, Any]]) -> None: ...


class ConnectionParameters(Parameters):

    class _DEFAULT:
        ...

    def __init__(
        self,
        host: Union[str, _DEFAULT] = ...,
        port: Union[int, _DEFAULT] = ...,
        virtual_host: Union[str, _DEFAULT] = ...,
        credentials: Union[credentials_.VALID_TYPES, _DEFAULT] = ...,
        channel_max: Union[int, _DEFAULT] = ...,
        frame_max: Union[int, _DEFAULT] = ...,
        heartbeat: Union[int, _OnHeartbeatTimeoutCallback, None, _DEFAULT] = ...,
        ssl_options: Union[SSLOptions, _DEFAULT] = ...,
        connection_attempts: Union[int, _DEFAULT] = ...,
        retry_delay: Union[numbers.Real, _DEFAULT] = ...,
        socket_timeout: Union[numbers.Real, _DEFAULT] = ...,
        stack_timeout: Union[numbers.Real, _DEFAULT] = ...,
        locale: Union[str, _DEFAULT] = ...,
        blocked_connection_timeout: Union[numbers.Real, None, _DEFAULT] = ...,
        client_properties: Union[Mapping[str, Any], None, _DEFAULT] = ...,
        tcp_options: Union[Mapping[str, Any], None, _DEFAULT] = ...,
        **kwargs: Any,
    ): ...


class URLParameters(Parameters):

    def __init__(self, url: str) -> None: ...


class SSLOptions:

    context: ssl.SSLContext = ...
    server_hostname: Optional[str] = ...

    def __init__(self, context: ssl.SSLContext, server_hostname: Optional[str] = ...): ...


class Connection(compat.AbstractBase):

    ON_CONNECTION_CLOSED: str = ...
    ON_CONNECTION_ERROR: str = ...
    ON_CONNECTION_OPEN_OK: str = ...

    CONNECTION_CLOSED: int = ...
    CONNECTION_INIT: int = ...
    CONNECTION_PROTOCOL: int = ...
    CONNECTION_START: int = ...
    CONNECTION_TUNE: int = ...
    CONNECTION_OPEN: int = ...
    CONNECTION_CLOSING: int = ...

    connection_state: Optional[str] = ...
    params: Optional[Parameters] = ...
    callbacks: callback.CallbackManager = ...
    server_capabilities: Optional[Mapping[str, Any]] = ...
    server_properties: Optional[Dict[str, Any]] = ...
    known_hosts: Optional[str] = ...

    bytes_sent: int = ...
    bytes_received: int = ...
    frames_sent: int = ...
    frames_received: int = ...

    def __init__(
        self,
        parameters: Optional[Parameters] = ...,
        on_open_callback: Optional[_OnOpenCallback] = ...,
        on_open_error_callback: Optional[_OnOpenErrorCallback] = ...,
        on_close_callback: Optional[_OnCloseCallback] = ...,
        internal_connection_workflow: bool = ...,
    ) -> None: ...

    def add_on_close_callback(self, callback: _OnCloseCallback) -> None: ...

    def add_on_connection_blocked_callback(
        self,
        callback: _OnConnectionBlockedCallback,
    ) -> None: ...

    def add_on_connection_unblocked_callback(
        self,
        callback: _OnConnectionUnblockedCallback,
    ) -> None: ...

    def add_on_open_callback(self, callback: _OnOpenCallback) -> None: ...

    def add_on_open_error_callback(
        self,
        callback: _OnOpenErrorCallback,
        remove_default: bool = ...,
    ) -> None: ...

    def channel(
        self,
        channel_number: Optional[int] = ...,
        on_open_callback: Optional[_OnOpenChannelCallback] = ...,
    ) -> channel_.Channel: ...

    def close(self, reply_code: int = ..., reply_text: str = ...) -> None: ...

    @property
    def is_closed(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_open(self) -> bool: ...
    @property
    def basic_nack(self) -> bool: ...
    @property
    def consumer_cancel_notify(self) -> bool: ...
    @property
    def exchange_exchange_bindings(self) -> bool: ...
    @property
    def publisher_confirms(self) -> bool: ...
