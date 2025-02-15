# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message
from google.protobuf.timestamp_pb2 import Timestamp

__all__ = [
    "GetTimeRequest",
    "GetTimeResponse",
    "SetTimeRequest",
]


class GetTimeRequest(_Message):
    ledger_id: _builtins.str
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetTimeResponse(_Message):
    @property
    def current_time(self) -> Timestamp: ...
    def __init__(self, *, current_time: _typing.Optional[Timestamp] = ...): ...
    def HasField(self, field_name: _typing.Literal["current_time"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _typing.Literal["current_time"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class SetTimeRequest(_Message):
    ledger_id: _builtins.str
    @property
    def current_time(self) -> Timestamp: ...
    @property
    def new_time(self) -> Timestamp: ...
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ..., current_time: _typing.Optional[Timestamp] = ..., new_time: _typing.Optional[Timestamp] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id", "current_time", "new_time"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id", "current_time", "new_time"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
