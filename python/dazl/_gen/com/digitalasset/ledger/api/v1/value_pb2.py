# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/ledger/api/v1/value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/digitalasset/ledger/api/v1/value.proto',
  package='com.digitalasset.ledger.api.v1',
  syntax='proto3',
  serialized_options=_b('\n\036com.digitalasset.ledger.api.v1B\017ValueOuterClass\252\002\036Com.DigitalAsset.Ledger.Api.V1'),
  serialized_pb=_b('\n*com/digitalasset/ledger/api/v1/value.proto\x12\x1e\x63om.digitalasset.ledger.api.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xa3\x04\n\x05Value\x12\x38\n\x06record\x18\x01 \x01(\x0b\x32&.com.digitalasset.ledger.api.v1.RecordH\x00\x12:\n\x07variant\x18\x02 \x01(\x0b\x32\'.com.digitalasset.ledger.api.v1.VariantH\x00\x12\x15\n\x0b\x63ontract_id\x18\x03 \x01(\tH\x00\x12\x34\n\x04list\x18\x04 \x01(\x0b\x32$.com.digitalasset.ledger.api.v1.ListH\x00\x12\x13\n\x05int64\x18\x05 \x01(\x12\x42\x02\x30\x01H\x00\x12\x11\n\x07numeric\x18\x06 \x01(\tH\x00\x12\x0e\n\x04text\x18\x08 \x01(\tH\x00\x12\x17\n\ttimestamp\x18\t \x01(\x10\x42\x02\x30\x01H\x00\x12\x0f\n\x05party\x18\x0b \x01(\tH\x00\x12\x0e\n\x04\x62ool\x18\x0c \x01(\x08H\x00\x12&\n\x04unit\x18\r \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x0e\n\x04\x64\x61te\x18\x0e \x01(\x05H\x00\x12<\n\x08optional\x18\x0f \x01(\x0b\x32(.com.digitalasset.ledger.api.v1.OptionalH\x00\x12\x32\n\x03map\x18\x10 \x01(\x0b\x32#.com.digitalasset.ledger.api.v1.MapH\x00\x12\x34\n\x04\x65num\x18\x11 \x01(\x0b\x32$.com.digitalasset.ledger.api.v1.EnumH\x00\x42\x05\n\x03Sum\"\x84\x01\n\x06Record\x12=\n\trecord_id\x18\x01 \x01(\x0b\x32*.com.digitalasset.ledger.api.v1.Identifier\x12;\n\x06\x66ields\x18\x02 \x03(\x0b\x32+.com.digitalasset.ledger.api.v1.RecordField\"R\n\x0bRecordField\x12\r\n\x05label\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.com.digitalasset.ledger.api.v1.Value\"P\n\nIdentifier\x12\x12\n\npackage_id\x18\x01 \x01(\t\x12\x13\n\x0bmodule_name\x18\x03 \x01(\t\x12\x13\n\x0b\x65ntity_name\x18\x04 \x01(\tJ\x04\x08\x02\x10\x03\"\x94\x01\n\x07Variant\x12>\n\nvariant_id\x18\x01 \x01(\x0b\x32*.com.digitalasset.ledger.api.v1.Identifier\x12\x13\n\x0b\x63onstructor\x18\x02 \x01(\t\x12\x34\n\x05value\x18\x03 \x01(\x0b\x32%.com.digitalasset.ledger.api.v1.Value\"X\n\x04\x45num\x12;\n\x07\x65num_id\x18\x01 \x01(\x0b\x32*.com.digitalasset.ledger.api.v1.Identifier\x12\x13\n\x0b\x63onstructor\x18\x02 \x01(\t\"?\n\x04List\x12\x37\n\x08\x65lements\x18\x01 \x03(\x0b\x32%.com.digitalasset.ledger.api.v1.Value\"@\n\x08Optional\x12\x34\n\x05value\x18\x01 \x01(\x0b\x32%.com.digitalasset.ledger.api.v1.Value\"\x8d\x01\n\x03Map\x12:\n\x07\x65ntries\x18\x01 \x03(\x0b\x32).com.digitalasset.ledger.api.v1.Map.Entry\x1aJ\n\x05\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.com.digitalasset.ledger.api.v1.ValueBR\n\x1e\x63om.digitalasset.ledger.api.v1B\x0fValueOuterClass\xaa\x02\x1e\x43om.DigitalAsset.Ledger.Api.V1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='com.digitalasset.ledger.api.v1.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='com.digitalasset.ledger.api.v1.Value.record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variant', full_name='com.digitalasset.ledger.api.v1.Value.variant', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='com.digitalasset.ledger.api.v1.Value.contract_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='com.digitalasset.ledger.api.v1.Value.list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64', full_name='com.digitalasset.ledger.api.v1.Value.int64', index=4,
      number=5, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('0\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numeric', full_name='com.digitalasset.ledger.api.v1.Value.numeric', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='com.digitalasset.ledger.api.v1.Value.text', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.digitalasset.ledger.api.v1.Value.timestamp', index=7,
      number=9, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('0\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='party', full_name='com.digitalasset.ledger.api.v1.Value.party', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool', full_name='com.digitalasset.ledger.api.v1.Value.bool', index=9,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='com.digitalasset.ledger.api.v1.Value.unit', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='com.digitalasset.ledger.api.v1.Value.date', index=11,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optional', full_name='com.digitalasset.ledger.api.v1.Value.optional', index=12,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map', full_name='com.digitalasset.ledger.api.v1.Value.map', index=13,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum', full_name='com.digitalasset.ledger.api.v1.Value.enum', index=14,
      number=17, type=11, cpp_type=10, label=1,
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
      name='Sum', full_name='com.digitalasset.ledger.api.v1.Value.Sum',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=173,
  serialized_end=720,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='com.digitalasset.ledger.api.v1.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='com.digitalasset.ledger.api.v1.Record.record_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='com.digitalasset.ledger.api.v1.Record.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=723,
  serialized_end=855,
)


_RECORDFIELD = _descriptor.Descriptor(
  name='RecordField',
  full_name='com.digitalasset.ledger.api.v1.RecordField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='com.digitalasset.ledger.api.v1.RecordField.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.digitalasset.ledger.api.v1.RecordField.value', index=1,
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
  ],
  serialized_start=857,
  serialized_end=939,
)


_IDENTIFIER = _descriptor.Descriptor(
  name='Identifier',
  full_name='com.digitalasset.ledger.api.v1.Identifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='com.digitalasset.ledger.api.v1.Identifier.package_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module_name', full_name='com.digitalasset.ledger.api.v1.Identifier.module_name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_name', full_name='com.digitalasset.ledger.api.v1.Identifier.entity_name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=941,
  serialized_end=1021,
)


_VARIANT = _descriptor.Descriptor(
  name='Variant',
  full_name='com.digitalasset.ledger.api.v1.Variant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_id', full_name='com.digitalasset.ledger.api.v1.Variant.variant_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constructor', full_name='com.digitalasset.ledger.api.v1.Variant.constructor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.digitalasset.ledger.api.v1.Variant.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1024,
  serialized_end=1172,
)


_ENUM = _descriptor.Descriptor(
  name='Enum',
  full_name='com.digitalasset.ledger.api.v1.Enum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enum_id', full_name='com.digitalasset.ledger.api.v1.Enum.enum_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constructor', full_name='com.digitalasset.ledger.api.v1.Enum.constructor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1174,
  serialized_end=1262,
)


_LIST = _descriptor.Descriptor(
  name='List',
  full_name='com.digitalasset.ledger.api.v1.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='com.digitalasset.ledger.api.v1.List.elements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1264,
  serialized_end=1327,
)


_OPTIONAL = _descriptor.Descriptor(
  name='Optional',
  full_name='com.digitalasset.ledger.api.v1.Optional',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='com.digitalasset.ledger.api.v1.Optional.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1329,
  serialized_end=1393,
)


_MAP_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='com.digitalasset.ledger.api.v1.Map.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.digitalasset.ledger.api.v1.Map.Entry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.digitalasset.ledger.api.v1.Map.Entry.value', index=1,
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
  ],
  serialized_start=1463,
  serialized_end=1537,
)

_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='com.digitalasset.ledger.api.v1.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='com.digitalasset.ledger.api.v1.Map.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MAP_ENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1396,
  serialized_end=1537,
)

_VALUE.fields_by_name['record'].message_type = _RECORD
_VALUE.fields_by_name['variant'].message_type = _VARIANT
_VALUE.fields_by_name['list'].message_type = _LIST
_VALUE.fields_by_name['unit'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_VALUE.fields_by_name['optional'].message_type = _OPTIONAL
_VALUE.fields_by_name['map'].message_type = _MAP
_VALUE.fields_by_name['enum'].message_type = _ENUM
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['record'])
_VALUE.fields_by_name['record'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['variant'])
_VALUE.fields_by_name['variant'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['contract_id'])
_VALUE.fields_by_name['contract_id'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['list'])
_VALUE.fields_by_name['list'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['int64'])
_VALUE.fields_by_name['int64'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['numeric'])
_VALUE.fields_by_name['numeric'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['text'])
_VALUE.fields_by_name['text'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['timestamp'])
_VALUE.fields_by_name['timestamp'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['party'])
_VALUE.fields_by_name['party'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['bool'])
_VALUE.fields_by_name['bool'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['unit'])
_VALUE.fields_by_name['unit'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['date'])
_VALUE.fields_by_name['date'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['optional'])
_VALUE.fields_by_name['optional'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['map'])
_VALUE.fields_by_name['map'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_VALUE.oneofs_by_name['Sum'].fields.append(
  _VALUE.fields_by_name['enum'])
_VALUE.fields_by_name['enum'].containing_oneof = _VALUE.oneofs_by_name['Sum']
_RECORD.fields_by_name['record_id'].message_type = _IDENTIFIER
_RECORD.fields_by_name['fields'].message_type = _RECORDFIELD
_RECORDFIELD.fields_by_name['value'].message_type = _VALUE
_VARIANT.fields_by_name['variant_id'].message_type = _IDENTIFIER
_VARIANT.fields_by_name['value'].message_type = _VALUE
_ENUM.fields_by_name['enum_id'].message_type = _IDENTIFIER
_LIST.fields_by_name['elements'].message_type = _VALUE
_OPTIONAL.fields_by_name['value'].message_type = _VALUE
_MAP_ENTRY.fields_by_name['value'].message_type = _VALUE
_MAP_ENTRY.containing_type = _MAP
_MAP.fields_by_name['entries'].message_type = _MAP_ENTRY
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['RecordField'] = _RECORDFIELD
DESCRIPTOR.message_types_by_name['Identifier'] = _IDENTIFIER
DESCRIPTOR.message_types_by_name['Variant'] = _VARIANT
DESCRIPTOR.message_types_by_name['Enum'] = _ENUM
DESCRIPTOR.message_types_by_name['List'] = _LIST
DESCRIPTOR.message_types_by_name['Optional'] = _OPTIONAL
DESCRIPTOR.message_types_by_name['Map'] = _MAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Value)
  })
_sym_db.RegisterMessage(Value)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Record)
  })
_sym_db.RegisterMessage(Record)

RecordField = _reflection.GeneratedProtocolMessageType('RecordField', (_message.Message,), {
  'DESCRIPTOR' : _RECORDFIELD,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.RecordField)
  })
_sym_db.RegisterMessage(RecordField)

Identifier = _reflection.GeneratedProtocolMessageType('Identifier', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIER,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Identifier)
  })
_sym_db.RegisterMessage(Identifier)

Variant = _reflection.GeneratedProtocolMessageType('Variant', (_message.Message,), {
  'DESCRIPTOR' : _VARIANT,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Variant)
  })
_sym_db.RegisterMessage(Variant)

Enum = _reflection.GeneratedProtocolMessageType('Enum', (_message.Message,), {
  'DESCRIPTOR' : _ENUM,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Enum)
  })
_sym_db.RegisterMessage(Enum)

List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
  'DESCRIPTOR' : _LIST,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.List)
  })
_sym_db.RegisterMessage(List)

Optional = _reflection.GeneratedProtocolMessageType('Optional', (_message.Message,), {
  'DESCRIPTOR' : _OPTIONAL,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Optional)
  })
_sym_db.RegisterMessage(Optional)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _MAP_ENTRY,
    '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
    # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Map.Entry)
    })
  ,
  'DESCRIPTOR' : _MAP,
  '__module__' : 'com.digitalasset.ledger.api.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Map)
  })
_sym_db.RegisterMessage(Map)
_sym_db.RegisterMessage(Map.Entry)


DESCRIPTOR._options = None
_VALUE.fields_by_name['int64']._options = None
_VALUE.fields_by_name['timestamp']._options = None
# @@protoc_insertion_point(module_scope)
