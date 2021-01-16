# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/command_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import commands_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_commands__pb2
from . import trace_context_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2
from . import transaction_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/command_service.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\030CommandServiceOuterClass\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,com/daml/ledger/api/v1/command_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a%com/daml/ledger/api/v1/commands.proto\x1a*com/daml/ledger/api/v1/trace_context.proto\x1a(com/daml/ledger/api/v1/transaction.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x88\x01\n\x14SubmitAndWaitRequest\x12\x32\n\x08\x63ommands\x18\x01 \x01(\x0b\x32 .com.daml.ledger.api.v1.Commands\x12<\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32$.com.daml.ledger.api.v1.TraceContext\"?\n%SubmitAndWaitForTransactionIdResponse\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\"_\n#SubmitAndWaitForTransactionResponse\x12\x38\n\x0btransaction\x18\x01 \x01(\x0b\x32#.com.daml.ledger.api.v1.Transaction\"g\n\'SubmitAndWaitForTransactionTreeResponse\x12<\n\x0btransaction\x18\x01 \x01(\x0b\x32\'.com.daml.ledger.api.v1.TransactionTree2\x94\x04\n\x0e\x43ommandService\x12U\n\rSubmitAndWait\x12,.com.daml.ledger.api.v1.SubmitAndWaitRequest\x1a\x16.google.protobuf.Empty\x12\x8c\x01\n\x1dSubmitAndWaitForTransactionId\x12,.com.daml.ledger.api.v1.SubmitAndWaitRequest\x1a=.com.daml.ledger.api.v1.SubmitAndWaitForTransactionIdResponse\x12\x88\x01\n\x1bSubmitAndWaitForTransaction\x12,.com.daml.ledger.api.v1.SubmitAndWaitRequest\x1a;.com.daml.ledger.api.v1.SubmitAndWaitForTransactionResponse\x12\x90\x01\n\x1fSubmitAndWaitForTransactionTree\x12,.com.daml.ledger.api.v1.SubmitAndWaitRequest\x1a?.com.daml.ledger.api.v1.SubmitAndWaitForTransactionTreeResponseBK\n\x16\x63om.daml.ledger.api.v1B\x18\x43ommandServiceOuterClass\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_commands__pb2.DESCRIPTOR,com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2.DESCRIPTOR,com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SUBMITANDWAITREQUEST = _descriptor.Descriptor(
  name='SubmitAndWaitRequest',
  full_name='com.daml.ledger.api.v1.SubmitAndWaitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='commands', full_name='com.daml.ledger.api.v1.SubmitAndWaitRequest.commands', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.daml.ledger.api.v1.SubmitAndWaitRequest.trace_context', index=1,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=227,
  serialized_end=363,
)


_SUBMITANDWAITFORTRANSACTIONIDRESPONSE = _descriptor.Descriptor(
  name='SubmitAndWaitForTransactionIdResponse',
  full_name='com.daml.ledger.api.v1.SubmitAndWaitForTransactionIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='com.daml.ledger.api.v1.SubmitAndWaitForTransactionIdResponse.transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=365,
  serialized_end=428,
)


_SUBMITANDWAITFORTRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='SubmitAndWaitForTransactionResponse',
  full_name='com.daml.ledger.api.v1.SubmitAndWaitForTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='com.daml.ledger.api.v1.SubmitAndWaitForTransactionResponse.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=430,
  serialized_end=525,
)


_SUBMITANDWAITFORTRANSACTIONTREERESPONSE = _descriptor.Descriptor(
  name='SubmitAndWaitForTransactionTreeResponse',
  full_name='com.daml.ledger.api.v1.SubmitAndWaitForTransactionTreeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='com.daml.ledger.api.v1.SubmitAndWaitForTransactionTreeResponse.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=527,
  serialized_end=630,
)

_SUBMITANDWAITREQUEST.fields_by_name['commands'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_commands__pb2._COMMANDS
_SUBMITANDWAITREQUEST.fields_by_name['trace_context'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_SUBMITANDWAITFORTRANSACTIONRESPONSE.fields_by_name['transaction'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2._TRANSACTION
_SUBMITANDWAITFORTRANSACTIONTREERESPONSE.fields_by_name['transaction'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2._TRANSACTIONTREE
DESCRIPTOR.message_types_by_name['SubmitAndWaitRequest'] = _SUBMITANDWAITREQUEST
DESCRIPTOR.message_types_by_name['SubmitAndWaitForTransactionIdResponse'] = _SUBMITANDWAITFORTRANSACTIONIDRESPONSE
DESCRIPTOR.message_types_by_name['SubmitAndWaitForTransactionResponse'] = _SUBMITANDWAITFORTRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['SubmitAndWaitForTransactionTreeResponse'] = _SUBMITANDWAITFORTRANSACTIONTREERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitAndWaitRequest = _reflection.GeneratedProtocolMessageType('SubmitAndWaitRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITANDWAITREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.command_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.SubmitAndWaitRequest)
  })
_sym_db.RegisterMessage(SubmitAndWaitRequest)

SubmitAndWaitForTransactionIdResponse = _reflection.GeneratedProtocolMessageType('SubmitAndWaitForTransactionIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITANDWAITFORTRANSACTIONIDRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.command_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.SubmitAndWaitForTransactionIdResponse)
  })
_sym_db.RegisterMessage(SubmitAndWaitForTransactionIdResponse)

SubmitAndWaitForTransactionResponse = _reflection.GeneratedProtocolMessageType('SubmitAndWaitForTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITANDWAITFORTRANSACTIONRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.command_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.SubmitAndWaitForTransactionResponse)
  })
_sym_db.RegisterMessage(SubmitAndWaitForTransactionResponse)

SubmitAndWaitForTransactionTreeResponse = _reflection.GeneratedProtocolMessageType('SubmitAndWaitForTransactionTreeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITANDWAITFORTRANSACTIONTREERESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.command_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.SubmitAndWaitForTransactionTreeResponse)
  })
_sym_db.RegisterMessage(SubmitAndWaitForTransactionTreeResponse)


DESCRIPTOR._options = None

_COMMANDSERVICE = _descriptor.ServiceDescriptor(
  name='CommandService',
  full_name='com.daml.ledger.api.v1.CommandService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=633,
  serialized_end=1165,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubmitAndWait',
    full_name='com.daml.ledger.api.v1.CommandService.SubmitAndWait',
    index=0,
    containing_service=None,
    input_type=_SUBMITANDWAITREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitAndWaitForTransactionId',
    full_name='com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransactionId',
    index=1,
    containing_service=None,
    input_type=_SUBMITANDWAITREQUEST,
    output_type=_SUBMITANDWAITFORTRANSACTIONIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitAndWaitForTransaction',
    full_name='com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransaction',
    index=2,
    containing_service=None,
    input_type=_SUBMITANDWAITREQUEST,
    output_type=_SUBMITANDWAITFORTRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitAndWaitForTransactionTree',
    full_name='com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransactionTree',
    index=3,
    containing_service=None,
    input_type=_SUBMITANDWAITREQUEST,
    output_type=_SUBMITANDWAITFORTRANSACTIONTREERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDSERVICE)

DESCRIPTOR.services_by_name['CommandService'] = _COMMANDSERVICE

# @@protoc_insertion_point(module_scope)
