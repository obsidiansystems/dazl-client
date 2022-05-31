# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/command_submission_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import commands_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_commands__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7com/daml/ledger/api/v1/command_submission_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a%com/daml/ledger/api/v1/commands.proto\x1a\x1bgoogle/protobuf/empty.proto\"M\n\rSubmitRequest\x12<\n\x08\x63ommands\x18\x01 \x01(\x0b\x32 .com.daml.ledger.api.v1.CommandsR\x08\x63ommands2c\n\x18\x43ommandSubmissionService\x12G\n\x06Submit\x12%.com.daml.ledger.api.v1.SubmitRequest\x1a\x16.google.protobuf.EmptyB\x9c\x01\n\x16\x63om.daml.ledger.api.v1B\"CommandSubmissionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3')



_SUBMITREQUEST = DESCRIPTOR.message_types_by_name['SubmitRequest']
SubmitRequest = _reflection.GeneratedProtocolMessageType('SubmitRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.command_submission_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.SubmitRequest)
  })
_sym_db.RegisterMessage(SubmitRequest)

_COMMANDSUBMISSIONSERVICE = DESCRIPTOR.services_by_name['CommandSubmissionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.daml.ledger.api.v1B\"CommandSubmissionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1'
  _SUBMITREQUEST._serialized_start=151
  _SUBMITREQUEST._serialized_end=228
  _COMMANDSUBMISSIONSERVICE._serialized_start=230
  _COMMANDSUBMISSIONSERVICE._serialized_end=329
# @@protoc_insertion_point(module_scope)
