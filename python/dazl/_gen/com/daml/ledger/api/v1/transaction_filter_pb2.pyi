# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.internal.containers import MessageMap, RepeatedCompositeFieldContainer
from google.protobuf.message import Message as _Message

from .value_pb2 import Identifier

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "TransactionFilter",
    "Filters",
    "InclusiveFilters",
]


class TransactionFilter(_Message):
    @property
    def filters_by_party(self) -> MessageMap[_builtins.str, Filters]: ...
    def __init__(self, *, filters_by_party: _typing.Optional[_typing.Mapping[_builtins.str, Filters]] = ...): ...
    def HasField(self, field_name: _L["filters_by_party"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["filters_by_party"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class Filters(_Message):
    @property
    def inclusive(self) -> InclusiveFilters: ...
    def __init__(self, *, inclusive: _typing.Optional[InclusiveFilters] = ...): ...
    def HasField(self, field_name: _L["inclusive"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["inclusive"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class InclusiveFilters(_Message):
    @property
    def template_ids(self) -> RepeatedCompositeFieldContainer[Identifier]: ...
    def __init__(self, *, template_ids: _typing.Optional[_typing.Iterable[Identifier]] = ...): ...
    def HasField(self, field_name: _L["template_ids"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["template_ids"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
