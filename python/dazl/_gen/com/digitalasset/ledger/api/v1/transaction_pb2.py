# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/ledger/api/v1/transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import event_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_event__pb2
from . import trace_context_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/digitalasset/ledger/api/v1/transaction.proto',
  package='com.digitalasset.ledger.api.v1',
  syntax='proto3',
  serialized_options=_b('\n\036com.digitalasset.ledger.api.v1B\025TransactionOuterClass\252\002\036Com.DigitalAsset.Ledger.Api.V1'),
  serialized_pb=_b('\n0com/digitalasset/ledger/api/v1/transaction.proto\x12\x1e\x63om.digitalasset.ledger.api.v1\x1a*com/digitalasset/ledger/api/v1/event.proto\x1a\x32\x63om/digitalasset/ledger/api/v1/trace_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa7\x03\n\x0fTransactionTree\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x12\n\ncommand_id\x18\x02 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x03 \x01(\t\x12\x30\n\x0c\x65\x66\x66\x65\x63tive_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06offset\x18\x06 \x01(\t\x12U\n\x0c\x65vents_by_id\x18\x07 \x03(\x0b\x32?.com.digitalasset.ledger.api.v1.TransactionTree.EventsByIdEntry\x12\x16\n\x0eroot_event_ids\x18\x08 \x03(\t\x12\x44\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.TraceContext\x1a\\\n\x0f\x45ventsByIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).com.digitalasset.ledger.api.v1.TreeEvent:\x02\x38\x01\"\x99\x01\n\tTreeEvent\x12?\n\x07\x63reated\x18\x01 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.CreatedEventH\x00\x12\x43\n\texercised\x18\x02 \x01(\x0b\x32..com.digitalasset.ledger.api.v1.ExercisedEventH\x00\x42\x06\n\x04kind\"\x8d\x02\n\x0bTransaction\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x12\n\ncommand_id\x18\x02 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x03 \x01(\t\x12\x30\n\x0c\x65\x66\x66\x65\x63tive_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x06\x65vents\x18\x05 \x03(\x0b\x32%.com.digitalasset.ledger.api.v1.Event\x12\x0e\n\x06offset\x18\x06 \x01(\t\x12\x44\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.TraceContextBX\n\x1e\x63om.digitalasset.ledger.api.v1B\x15TransactionOuterClass\xaa\x02\x1e\x43om.DigitalAsset.Ledger.Api.V1b\x06proto3')
  ,
  dependencies=[com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_event__pb2.DESCRIPTOR,com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_TRANSACTIONTREE_EVENTSBYIDENTRY = _descriptor.Descriptor(
  name='EventsByIdEntry',
  full_name='com.digitalasset.ledger.api.v1.TransactionTree.EventsByIdEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.digitalasset.ledger.api.v1.TransactionTree.EventsByIdEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.digitalasset.ledger.api.v1.TransactionTree.EventsByIdEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=545,
  serialized_end=637,
)

_TRANSACTIONTREE = _descriptor.Descriptor(
  name='TransactionTree',
  full_name='com.digitalasset.ledger.api.v1.TransactionTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='com.digitalasset.ledger.api.v1.TransactionTree.transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command_id', full_name='com.digitalasset.ledger.api.v1.TransactionTree.command_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='com.digitalasset.ledger.api.v1.TransactionTree.workflow_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effective_at', full_name='com.digitalasset.ledger.api.v1.TransactionTree.effective_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='com.digitalasset.ledger.api.v1.TransactionTree.offset', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events_by_id', full_name='com.digitalasset.ledger.api.v1.TransactionTree.events_by_id', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_event_ids', full_name='com.digitalasset.ledger.api.v1.TransactionTree.root_event_ids', index=6,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.digitalasset.ledger.api.v1.TransactionTree.trace_context', index=7,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTIONTREE_EVENTSBYIDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=637,
)


_TREEEVENT = _descriptor.Descriptor(
  name='TreeEvent',
  full_name='com.digitalasset.ledger.api.v1.TreeEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='com.digitalasset.ledger.api.v1.TreeEvent.created', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exercised', full_name='com.digitalasset.ledger.api.v1.TreeEvent.exercised', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='com.digitalasset.ledger.api.v1.TreeEvent.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=640,
  serialized_end=793,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='com.digitalasset.ledger.api.v1.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='com.digitalasset.ledger.api.v1.Transaction.transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command_id', full_name='com.digitalasset.ledger.api.v1.Transaction.command_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='com.digitalasset.ledger.api.v1.Transaction.workflow_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effective_at', full_name='com.digitalasset.ledger.api.v1.Transaction.effective_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='com.digitalasset.ledger.api.v1.Transaction.events', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='com.digitalasset.ledger.api.v1.Transaction.offset', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.digitalasset.ledger.api.v1.Transaction.trace_context', index=6,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=796,
  serialized_end=1065,
)

_TRANSACTIONTREE_EVENTSBYIDENTRY.fields_by_name['value'].message_type = _TREEEVENT
_TRANSACTIONTREE_EVENTSBYIDENTRY.containing_type = _TRANSACTIONTREE
_TRANSACTIONTREE.fields_by_name['effective_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSACTIONTREE.fields_by_name['events_by_id'].message_type = _TRANSACTIONTREE_EVENTSBYIDENTRY
_TRANSACTIONTREE.fields_by_name['trace_context'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_TREEEVENT.fields_by_name['created'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_event__pb2._CREATEDEVENT
_TREEEVENT.fields_by_name['exercised'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_event__pb2._EXERCISEDEVENT
_TREEEVENT.oneofs_by_name['kind'].fields.append(
  _TREEEVENT.fields_by_name['created'])
_TREEEVENT.fields_by_name['created'].containing_oneof = _TREEEVENT.oneofs_by_name['kind']
_TREEEVENT.oneofs_by_name['kind'].fields.append(
  _TREEEVENT.fields_by_name['exercised'])
_TREEEVENT.fields_by_name['exercised'].containing_oneof = _TREEEVENT.oneofs_by_name['kind']
_TRANSACTION.fields_by_name['effective_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSACTION.fields_by_name['events'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_event__pb2._EVENT
_TRANSACTION.fields_by_name['trace_context'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
DESCRIPTOR.message_types_by_name['TransactionTree'] = _TRANSACTIONTREE
DESCRIPTOR.message_types_by_name['TreeEvent'] = _TREEEVENT
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionTree = _reflection.GeneratedProtocolMessageType('TransactionTree', (_message.Message,), dict(

  EventsByIdEntry = _reflection.GeneratedProtocolMessageType('EventsByIdEntry', (_message.Message,), dict(
    DESCRIPTOR = _TRANSACTIONTREE_EVENTSBYIDENTRY,
    __module__ = 'com.digitalasset.ledger.api.v1.transaction_pb2'
    # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.TransactionTree.EventsByIdEntry)
    ))
  ,
  DESCRIPTOR = _TRANSACTIONTREE,
  __module__ = 'com.digitalasset.ledger.api.v1.transaction_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.TransactionTree)
  ))
_sym_db.RegisterMessage(TransactionTree)
_sym_db.RegisterMessage(TransactionTree.EventsByIdEntry)

TreeEvent = _reflection.GeneratedProtocolMessageType('TreeEvent', (_message.Message,), dict(
  DESCRIPTOR = _TREEEVENT,
  __module__ = 'com.digitalasset.ledger.api.v1.transaction_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.TreeEvent)
  ))
_sym_db.RegisterMessage(TreeEvent)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'com.digitalasset.ledger.api.v1.transaction_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)


DESCRIPTOR._options = None
_TRANSACTIONTREE_EVENTSBYIDENTRY._options = None
# @@protoc_insertion_point(module_scope)
