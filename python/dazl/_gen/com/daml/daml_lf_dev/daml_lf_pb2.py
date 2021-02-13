# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/daml_lf_dev/daml_lf.proto

from google.protobuf import (
    descriptor as _descriptor,
    message as _message,
    reflection as _reflection,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import daml_lf_1_pb2 as com_dot_daml_dot_daml__lf__dev_dot_daml__lf__1__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="com/daml/daml_lf_dev/daml_lf.proto",
    package="daml_lf_dev",
    syntax="proto3",
    serialized_options=b"\n\024com.daml.daml_lf_dev\252\002\033Com.Daml.Daml_Lf_Dev.DamlLf",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n"com/daml/daml_lf_dev/daml_lf.proto\x12\x0b\x64\x61ml_lf_dev\x1a$com/daml/daml_lf_dev/daml_lf_1.proto"]\n\x0e\x41rchivePayload\x12\r\n\x05minor\x18\x03 \x01(\t\x12\'\n\tdaml_lf_1\x18\x02 \x01(\x0b\x32\x12.daml_lf_1.PackageH\x00\x42\x05\n\x03SumJ\x06\x08\x8fN\x10\x90NJ\x04\x08\x01\x10\x02"Z\n\x07\x41rchive\x12\x30\n\rhash_function\x18\x01 \x01(\x0e\x32\x19.daml_lf_dev.HashFunction\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x0c\n\x04hash\x18\x04 \x01(\t*\x1a\n\x0cHashFunction\x12\n\n\x06SHA256\x10\x00\x42\x34\n\x14\x63om.daml.daml_lf_dev\xaa\x02\x1b\x43om.Daml.Daml_Lf_Dev.DamlLfb\x06proto3',
    dependencies=[
        com_dot_daml_dot_daml__lf__dev_dot_daml__lf__1__pb2.DESCRIPTOR,
    ],
)

_HASHFUNCTION = _descriptor.EnumDescriptor(
    name="HashFunction",
    full_name="daml_lf_dev.HashFunction",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SHA256",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=276,
    serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_HASHFUNCTION)

HashFunction = enum_type_wrapper.EnumTypeWrapper(_HASHFUNCTION)
SHA256 = 0


_ARCHIVEPAYLOAD = _descriptor.Descriptor(
    name="ArchivePayload",
    full_name="daml_lf_dev.ArchivePayload",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="minor",
            full_name="daml_lf_dev.ArchivePayload.minor",
            index=0,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="daml_lf_1",
            full_name="daml_lf_dev.ArchivePayload.daml_lf_1",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="Sum",
            full_name="daml_lf_dev.ArchivePayload.Sum",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=89,
    serialized_end=182,
)


_ARCHIVE = _descriptor.Descriptor(
    name="Archive",
    full_name="daml_lf_dev.Archive",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="hash_function",
            full_name="daml_lf_dev.Archive.hash_function",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="daml_lf_dev.Archive.payload",
            index=1,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="hash",
            full_name="daml_lf_dev.Archive.hash",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=184,
    serialized_end=274,
)

_ARCHIVEPAYLOAD.fields_by_name[
    "daml_lf_1"
].message_type = com_dot_daml_dot_daml__lf__dev_dot_daml__lf__1__pb2._PACKAGE
_ARCHIVEPAYLOAD.oneofs_by_name["Sum"].fields.append(_ARCHIVEPAYLOAD.fields_by_name["daml_lf_1"])
_ARCHIVEPAYLOAD.fields_by_name["daml_lf_1"].containing_oneof = _ARCHIVEPAYLOAD.oneofs_by_name["Sum"]
_ARCHIVE.fields_by_name["hash_function"].enum_type = _HASHFUNCTION
DESCRIPTOR.message_types_by_name["ArchivePayload"] = _ARCHIVEPAYLOAD
DESCRIPTOR.message_types_by_name["Archive"] = _ARCHIVE
DESCRIPTOR.enum_types_by_name["HashFunction"] = _HASHFUNCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArchivePayload = _reflection.GeneratedProtocolMessageType(
    "ArchivePayload",
    (_message.Message,),
    {
        "DESCRIPTOR": _ARCHIVEPAYLOAD,
        "__module__": "com.daml.daml_lf_dev.daml_lf_pb2"
        # @@protoc_insertion_point(class_scope:daml_lf_dev.ArchivePayload)
    },
)
_sym_db.RegisterMessage(ArchivePayload)

Archive = _reflection.GeneratedProtocolMessageType(
    "Archive",
    (_message.Message,),
    {
        "DESCRIPTOR": _ARCHIVE,
        "__module__": "com.daml.daml_lf_dev.daml_lf_pb2"
        # @@protoc_insertion_point(class_scope:daml_lf_dev.Archive)
    },
)
_sym_db.RegisterMessage(Archive)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
