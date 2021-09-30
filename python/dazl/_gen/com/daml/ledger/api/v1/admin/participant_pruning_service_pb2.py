# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/admin/participant_pruning_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/admin/participant_pruning_service.proto',
  package='com.daml.ledger.api.v1.admin',
  syntax='proto3',
  serialized_options=b'\n\034com.daml.ledger.api.v1.adminB#ParticipantPruningServiceOuterClassZUgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1/admin\252\002\034Com.Daml.Ledger.Api.V1.Admin',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>com/daml/ledger/api/v1/admin/participant_pruning_service.proto\x12\x1c\x63om.daml.ledger.api.v1.admin\"\x94\x01\n\x0cPruneRequest\x12\x1e\n\x0bprune_up_to\x18\x01 \x01(\tR\tpruneUpTo\x12#\n\rsubmission_id\x18\x02 \x01(\tR\x0csubmissionId\x12?\n\x1cprune_all_divulged_contracts\x18\x03 \x01(\x08R\x19pruneAllDivulgedContracts\"\x0f\n\rPruneResponse2}\n\x19ParticipantPruningService\x12`\n\x05Prune\x12*.com.daml.ledger.api.v1.admin.PruneRequest\x1a+.com.daml.ledger.api.v1.admin.PruneResponseB\xb9\x01\n\x1c\x63om.daml.ledger.api.v1.adminB#ParticipantPruningServiceOuterClassZUgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1/admin\xaa\x02\x1c\x43om.Daml.Ledger.Api.V1.Adminb\x06proto3'
)




_PRUNEREQUEST = _descriptor.Descriptor(
  name='PruneRequest',
  full_name='com.daml.ledger.api.v1.admin.PruneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prune_up_to', full_name='com.daml.ledger.api.v1.admin.PruneRequest.prune_up_to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pruneUpTo', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submission_id', full_name='com.daml.ledger.api.v1.admin.PruneRequest.submission_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='submissionId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prune_all_divulged_contracts', full_name='com.daml.ledger.api.v1.admin.PruneRequest.prune_all_divulged_contracts', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pruneAllDivulgedContracts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=97,
  serialized_end=245,
)


_PRUNERESPONSE = _descriptor.Descriptor(
  name='PruneResponse',
  full_name='com.daml.ledger.api.v1.admin.PruneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=247,
  serialized_end=262,
)

DESCRIPTOR.message_types_by_name['PruneRequest'] = _PRUNEREQUEST
DESCRIPTOR.message_types_by_name['PruneResponse'] = _PRUNERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PruneRequest = _reflection.GeneratedProtocolMessageType('PruneRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRUNEREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.participant_pruning_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.PruneRequest)
  })
_sym_db.RegisterMessage(PruneRequest)

PruneResponse = _reflection.GeneratedProtocolMessageType('PruneResponse', (_message.Message,), {
  'DESCRIPTOR' : _PRUNERESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.participant_pruning_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.PruneResponse)
  })
_sym_db.RegisterMessage(PruneResponse)


DESCRIPTOR._options = None

_PARTICIPANTPRUNINGSERVICE = _descriptor.ServiceDescriptor(
  name='ParticipantPruningService',
  full_name='com.daml.ledger.api.v1.admin.ParticipantPruningService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=264,
  serialized_end=389,
  methods=[
  _descriptor.MethodDescriptor(
    name='Prune',
    full_name='com.daml.ledger.api.v1.admin.ParticipantPruningService.Prune',
    index=0,
    containing_service=None,
    input_type=_PRUNEREQUEST,
    output_type=_PRUNERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PARTICIPANTPRUNINGSERVICE)

DESCRIPTOR.services_by_name['ParticipantPruningService'] = _PARTICIPANTPRUNINGSERVICE

# @@protoc_insertion_point(module_scope)
