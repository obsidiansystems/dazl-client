# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

from typing import (
    Any as __Any,
    Dict as __Map,
    List as __List,
    Literal as __Literal,
    Mapping as __Mapping,
    NoReturn as __Void,
    Optional as __Optional,
    Sequence as __Sequence,
    Tuple as __Tuple,
    overload,
)

from google.protobuf.descriptor import FieldDescriptor as __FieldDescriptor
from google.protobuf.message import Message as __Message

from .......damlast.daml_types import Party
from .ledger_offset_pb2 import LedgerOffset
from .trace_context_pb2 import TraceContext
from .transaction_filter_pb2 import TransactionFilter
from .transaction_pb2 import Transaction, TransactionTree

__all__ = [
    "GetTransactionsRequest",
    "GetTransactionsResponse",
    "GetTransactionTreesResponse",
    "GetTransactionByEventIdRequest",
    "GetTransactionByIdRequest",
    "GetTransactionResponse",
    "GetFlatTransactionResponse",
    "GetLedgerEndRequest",
    "GetLedgerEndResponse",
]

class GetTransactionsRequest(__Message):
    ledger_id: str
    begin: LedgerOffset
    end: LedgerOffset
    filter: TransactionFilter
    verbose: bool
    trace_context: TraceContext
    def __init__(self, ledger_id: str = ..., begin: LedgerOffset = ..., end: LedgerOffset = ..., filter: TransactionFilter = ..., verbose: bool = ..., trace_context: TraceContext = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetTransactionsRequest) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["ledger_id", "begin", "end", "filter", "verbose", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: __Literal["ledger_id", "begin", "end", "filter", "verbose", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetTransactionsResponse(__Message):
    transactions: __List[Transaction]
    def __init__(self, transactions: __Sequence[Transaction] = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetTransactionResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["transactions"]) -> bool: ...
    def ClearField(self, field_name: __Literal["transactions"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetTransactionTreesResponse(__Message):
    transactions: __List[TransactionTree]
    def __init__(self, transactions: __Sequence[TransactionTree] = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetTransactionTreesResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["transactions"]) -> bool: ...
    def ClearField(self, field_name: __Literal["transactions"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetTransactionByEventIdRequest(__Message):
    ledger_id: str
    event_id: str
    requesting_parties: __List[Party]
    trace_context: TraceContext
    def __init__(self, ledger_id: str = ..., event_id: str = ..., requesting_parties: __Sequence[Party] = ..., trace_context: TraceContext = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetTransactionByEventIdRequest) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["ledger_id", "event_id", "requesting_parties", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: __Literal["ledger_id", "event_id", "requesting_parties", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetTransactionByIdRequest(__Message):
    ledger_id: str
    event_id: str
    requesting_parties: __List[Party]
    trace_context: TraceContext
    def __init__(self, ledger_id: str = ..., event_id: str = ..., requesting_parties: __Sequence[Party] = ..., trace_context: TraceContext = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetTransactionByIdRequest) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["ledger_id", "event_id", "requesting_parties", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: __Literal["ledger_id", "event_id", "requesting_parties", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetTransactionResponse(__Message):
    transaction: TransactionTree
    def __init__(self, transaction: TransactionTree = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetTransactionResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["transaction"]) -> bool: ...
    def ClearField(self, field_name: __Literal["transaction"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetFlatTransactionResponse(__Message):
    transaction: Transaction
    def __init__(self, transaction: Transaction = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetFlatTransactionResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["transaction"]) -> bool: ...
    def ClearField(self, field_name: __Literal["transaction"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetLedgerEndRequest(__Message):
    ledger_id: str
    trace_context: TraceContext
    def __init__(self, ledger_id: str = ..., trace_context: TraceContext = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetLedgerEndRequest) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["ledger_id", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: __Literal["ledger_id", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetLedgerEndResponse(__Message):
    offset: LedgerOffset
    def __init__(self, offset: LedgerOffset = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetLedgerEndResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["offset"]) -> bool: ...
    def ClearField(self, field_name: __Literal["offset"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...
