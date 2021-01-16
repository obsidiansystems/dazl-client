# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/commands.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import value_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/commands.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\022CommandsOuterClass\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%com/daml/ledger/api/v1/commands.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\"com/daml/ledger/api/v1/value.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xf5\x02\n\x08\x43ommands\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x02 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x03 \x01(\t\x12\x12\n\ncommand_id\x18\x04 \x01(\t\x12\r\n\x05party\x18\x05 \x01(\t\x12\x31\n\x08\x63ommands\x18\x08 \x03(\x0b\x32\x1f.com.daml.ledger.api.v1.Command\x12\x35\n\x12\x64\x65\x64uplication_time\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x13min_ledger_time_abs\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x13min_ledger_time_rel\x18\x0b \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0e\n\x06\x61\x63t_as\x18\x0c \x03(\t\x12\x0f\n\x07read_as\x18\r \x03(\tJ\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08\"\xa0\x02\n\x07\x43ommand\x12\x37\n\x06\x63reate\x18\x01 \x01(\x0b\x32%.com.daml.ledger.api.v1.CreateCommandH\x00\x12;\n\x08\x65xercise\x18\x02 \x01(\x0b\x32\'.com.daml.ledger.api.v1.ExerciseCommandH\x00\x12\x45\n\rexerciseByKey\x18\x04 \x01(\x0b\x32,.com.daml.ledger.api.v1.ExerciseByKeyCommandH\x00\x12M\n\x11\x63reateAndExercise\x18\x03 \x01(\x0b\x32\x30.com.daml.ledger.api.v1.CreateAndExerciseCommandH\x00\x42\t\n\x07\x63ommand\"\x82\x01\n\rCreateCommand\x12\x37\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.Identifier\x12\x38\n\x10\x63reate_arguments\x18\x02 \x01(\x0b\x32\x1e.com.daml.ledger.api.v1.Record\"\xa7\x01\n\x0f\x45xerciseCommand\x12\x37\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.Identifier\x12\x13\n\x0b\x63ontract_id\x18\x02 \x01(\t\x12\x0e\n\x06\x63hoice\x18\x03 \x01(\t\x12\x36\n\x0f\x63hoice_argument\x18\x04 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.Value\"\xcc\x01\n\x14\x45xerciseByKeyCommand\x12\x37\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.Identifier\x12\x33\n\x0c\x63ontract_key\x18\x02 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.Value\x12\x0e\n\x06\x63hoice\x18\x03 \x01(\t\x12\x36\n\x0f\x63hoice_argument\x18\x04 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.Value\"\xd5\x01\n\x18\x43reateAndExerciseCommand\x12\x37\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.Identifier\x12\x38\n\x10\x63reate_arguments\x18\x02 \x01(\x0b\x32\x1e.com.daml.ledger.api.v1.Record\x12\x0e\n\x06\x63hoice\x18\x03 \x01(\t\x12\x36\n\x0f\x63hoice_argument\x18\x04 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueBE\n\x16\x63om.daml.ledger.api.v1B\x12\x43ommandsOuterClass\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_COMMANDS = _descriptor.Descriptor(
  name='Commands',
  full_name='com.daml.ledger.api.v1.Commands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.Commands.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='com.daml.ledger.api.v1.Commands.workflow_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application_id', full_name='com.daml.ledger.api.v1.Commands.application_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_id', full_name='com.daml.ledger.api.v1.Commands.command_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='party', full_name='com.daml.ledger.api.v1.Commands.party', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commands', full_name='com.daml.ledger.api.v1.Commands.commands', index=5,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deduplication_time', full_name='com.daml.ledger.api.v1.Commands.deduplication_time', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_ledger_time_abs', full_name='com.daml.ledger.api.v1.Commands.min_ledger_time_abs', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_ledger_time_rel', full_name='com.daml.ledger.api.v1.Commands.min_ledger_time_rel', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='act_as', full_name='com.daml.ledger.api.v1.Commands.act_as', index=9,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read_as', full_name='com.daml.ledger.api.v1.Commands.read_as', index=10,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=167,
  serialized_end=540,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='com.daml.ledger.api.v1.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='com.daml.ledger.api.v1.Command.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exercise', full_name='com.daml.ledger.api.v1.Command.exercise', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exerciseByKey', full_name='com.daml.ledger.api.v1.Command.exerciseByKey', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createAndExercise', full_name='com.daml.ledger.api.v1.Command.createAndExercise', index=3,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='command', full_name='com.daml.ledger.api.v1.Command.command',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=543,
  serialized_end=831,
)


_CREATECOMMAND = _descriptor.Descriptor(
  name='CreateCommand',
  full_name='com.daml.ledger.api.v1.CreateCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.daml.ledger.api.v1.CreateCommand.template_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_arguments', full_name='com.daml.ledger.api.v1.CreateCommand.create_arguments', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=834,
  serialized_end=964,
)


_EXERCISECOMMAND = _descriptor.Descriptor(
  name='ExerciseCommand',
  full_name='com.daml.ledger.api.v1.ExerciseCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.daml.ledger.api.v1.ExerciseCommand.template_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='com.daml.ledger.api.v1.ExerciseCommand.contract_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice', full_name='com.daml.ledger.api.v1.ExerciseCommand.choice', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice_argument', full_name='com.daml.ledger.api.v1.ExerciseCommand.choice_argument', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=967,
  serialized_end=1134,
)


_EXERCISEBYKEYCOMMAND = _descriptor.Descriptor(
  name='ExerciseByKeyCommand',
  full_name='com.daml.ledger.api.v1.ExerciseByKeyCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.daml.ledger.api.v1.ExerciseByKeyCommand.template_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_key', full_name='com.daml.ledger.api.v1.ExerciseByKeyCommand.contract_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice', full_name='com.daml.ledger.api.v1.ExerciseByKeyCommand.choice', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice_argument', full_name='com.daml.ledger.api.v1.ExerciseByKeyCommand.choice_argument', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1137,
  serialized_end=1341,
)


_CREATEANDEXERCISECOMMAND = _descriptor.Descriptor(
  name='CreateAndExerciseCommand',
  full_name='com.daml.ledger.api.v1.CreateAndExerciseCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.daml.ledger.api.v1.CreateAndExerciseCommand.template_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_arguments', full_name='com.daml.ledger.api.v1.CreateAndExerciseCommand.create_arguments', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice', full_name='com.daml.ledger.api.v1.CreateAndExerciseCommand.choice', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice_argument', full_name='com.daml.ledger.api.v1.CreateAndExerciseCommand.choice_argument', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1344,
  serialized_end=1557,
)

_COMMANDS.fields_by_name['commands'].message_type = _COMMAND
_COMMANDS.fields_by_name['deduplication_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_COMMANDS.fields_by_name['min_ledger_time_abs'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_COMMANDS.fields_by_name['min_ledger_time_rel'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_COMMAND.fields_by_name['create'].message_type = _CREATECOMMAND
_COMMAND.fields_by_name['exercise'].message_type = _EXERCISECOMMAND
_COMMAND.fields_by_name['exerciseByKey'].message_type = _EXERCISEBYKEYCOMMAND
_COMMAND.fields_by_name['createAndExercise'].message_type = _CREATEANDEXERCISECOMMAND
_COMMAND.oneofs_by_name['command'].fields.append(
  _COMMAND.fields_by_name['create'])
_COMMAND.fields_by_name['create'].containing_oneof = _COMMAND.oneofs_by_name['command']
_COMMAND.oneofs_by_name['command'].fields.append(
  _COMMAND.fields_by_name['exercise'])
_COMMAND.fields_by_name['exercise'].containing_oneof = _COMMAND.oneofs_by_name['command']
_COMMAND.oneofs_by_name['command'].fields.append(
  _COMMAND.fields_by_name['exerciseByKey'])
_COMMAND.fields_by_name['exerciseByKey'].containing_oneof = _COMMAND.oneofs_by_name['command']
_COMMAND.oneofs_by_name['command'].fields.append(
  _COMMAND.fields_by_name['createAndExercise'])
_COMMAND.fields_by_name['createAndExercise'].containing_oneof = _COMMAND.oneofs_by_name['command']
_CREATECOMMAND.fields_by_name['template_id'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_CREATECOMMAND.fields_by_name['create_arguments'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._RECORD
_EXERCISECOMMAND.fields_by_name['template_id'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_EXERCISECOMMAND.fields_by_name['choice_argument'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
_EXERCISEBYKEYCOMMAND.fields_by_name['template_id'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_EXERCISEBYKEYCOMMAND.fields_by_name['contract_key'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
_EXERCISEBYKEYCOMMAND.fields_by_name['choice_argument'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
_CREATEANDEXERCISECOMMAND.fields_by_name['template_id'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_CREATEANDEXERCISECOMMAND.fields_by_name['create_arguments'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._RECORD
_CREATEANDEXERCISECOMMAND.fields_by_name['choice_argument'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
DESCRIPTOR.message_types_by_name['Commands'] = _COMMANDS
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['CreateCommand'] = _CREATECOMMAND
DESCRIPTOR.message_types_by_name['ExerciseCommand'] = _EXERCISECOMMAND
DESCRIPTOR.message_types_by_name['ExerciseByKeyCommand'] = _EXERCISEBYKEYCOMMAND
DESCRIPTOR.message_types_by_name['CreateAndExerciseCommand'] = _CREATEANDEXERCISECOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Commands = _reflection.GeneratedProtocolMessageType('Commands', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDS,
  '__module__' : 'com.daml.ledger.api.v1.commands_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.Commands)
  })
_sym_db.RegisterMessage(Commands)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'com.daml.ledger.api.v1.commands_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.Command)
  })
_sym_db.RegisterMessage(Command)

CreateCommand = _reflection.GeneratedProtocolMessageType('CreateCommand', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOMMAND,
  '__module__' : 'com.daml.ledger.api.v1.commands_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CreateCommand)
  })
_sym_db.RegisterMessage(CreateCommand)

ExerciseCommand = _reflection.GeneratedProtocolMessageType('ExerciseCommand', (_message.Message,), {
  'DESCRIPTOR' : _EXERCISECOMMAND,
  '__module__' : 'com.daml.ledger.api.v1.commands_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ExerciseCommand)
  })
_sym_db.RegisterMessage(ExerciseCommand)

ExerciseByKeyCommand = _reflection.GeneratedProtocolMessageType('ExerciseByKeyCommand', (_message.Message,), {
  'DESCRIPTOR' : _EXERCISEBYKEYCOMMAND,
  '__module__' : 'com.daml.ledger.api.v1.commands_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ExerciseByKeyCommand)
  })
_sym_db.RegisterMessage(ExerciseByKeyCommand)

CreateAndExerciseCommand = _reflection.GeneratedProtocolMessageType('CreateAndExerciseCommand', (_message.Message,), {
  'DESCRIPTOR' : _CREATEANDEXERCISECOMMAND,
  '__module__' : 'com.daml.ledger.api.v1.commands_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CreateAndExerciseCommand)
  })
_sym_db.RegisterMessage(CreateAndExerciseCommand)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
