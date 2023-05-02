# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/completion.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'com/daml/ledger/api/v1/completion.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto\"\x99\x03\n\nCompletion\x12\x1d\n\ncommand_id\x18\x01 \x01(\tR\tcommandId\x12*\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status\x12%\n\x0etransaction_id\x18\x03 \x01(\tR\rtransactionId\x12%\n\x0e\x61pplication_id\x18\x04 \x01(\tR\rapplicationId\x12\x15\n\x06\x61\x63t_as\x18\x05 \x03(\tR\x05\x61\x63tAs\x12#\n\rsubmission_id\x18\x06 \x01(\tR\x0csubmissionId\x12\x33\n\x14\x64\x65\x64uplication_offset\x18\x08 \x01(\tH\x00R\x13\x64\x65\x64uplicationOffset\x12R\n\x16\x64\x65\x64uplication_duration\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationH\x00R\x15\x64\x65\x64uplicationDurationB\x16\n\x14\x64\x65\x64uplication_periodJ\x04\x08\x07\x10\x08R\x0fsubmission_rankB\x8e\x01\n\x16\x63om.daml.ledger.api.v1B\x14\x43ompletionOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.completion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.daml.ledger.api.v1B\024CompletionOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1'
  _COMPLETION._serialized_start=125
  _COMPLETION._serialized_end=534
# @@protoc_insertion_point(module_scope)
