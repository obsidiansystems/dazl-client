# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/admin/party_management_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;com/daml/ledger/api/v1/admin/party_management_service.proto\x12\x1c\x63om.daml.ledger.api.v1.admin\"\x19\n\x17GetParticipantIdRequest\"A\n\x18GetParticipantIdResponse\x12%\n\x0eparticipant_id\x18\x01 \x01(\tR\rparticipantId\"-\n\x11GetPartiesRequest\x12\x18\n\x07parties\x18\x01 \x03(\tR\x07parties\"e\n\x12GetPartiesResponse\x12O\n\rparty_details\x18\x01 \x03(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetailsR\x0cpartyDetails\"\x19\n\x17ListKnownPartiesRequest\"k\n\x18ListKnownPartiesResponse\x12O\n\rparty_details\x18\x01 \x03(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetailsR\x0cpartyDetails\"]\n\x14\x41llocatePartyRequest\x12\"\n\rparty_id_hint\x18\x01 \x01(\tR\x0bpartyIdHint\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\"h\n\x15\x41llocatePartyResponse\x12O\n\rparty_details\x18\x01 \x01(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetailsR\x0cpartyDetails\"b\n\x0cPartyDetails\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x19\n\x08is_local\x18\x03 \x01(\x08R\x07isLocal2\x8b\x04\n\x16PartyManagementService\x12\x81\x01\n\x10GetParticipantId\x12\x35.com.daml.ledger.api.v1.admin.GetParticipantIdRequest\x1a\x36.com.daml.ledger.api.v1.admin.GetParticipantIdResponse\x12o\n\nGetParties\x12/.com.daml.ledger.api.v1.admin.GetPartiesRequest\x1a\x30.com.daml.ledger.api.v1.admin.GetPartiesResponse\x12\x81\x01\n\x10ListKnownParties\x12\x35.com.daml.ledger.api.v1.admin.ListKnownPartiesRequest\x1a\x36.com.daml.ledger.api.v1.admin.ListKnownPartiesResponse\x12x\n\rAllocateParty\x12\x32.com.daml.ledger.api.v1.admin.AllocatePartyRequest\x1a\x33.com.daml.ledger.api.v1.admin.AllocatePartyResponseB\xac\x01\n\x1c\x63om.daml.ledger.api.v1.adminB PartyManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1/admin\xaa\x02\x1c\x43om.Daml.Ledger.Api.V1.Adminb\x06proto3')



_GETPARTICIPANTIDREQUEST = DESCRIPTOR.message_types_by_name['GetParticipantIdRequest']
_GETPARTICIPANTIDRESPONSE = DESCRIPTOR.message_types_by_name['GetParticipantIdResponse']
_GETPARTIESREQUEST = DESCRIPTOR.message_types_by_name['GetPartiesRequest']
_GETPARTIESRESPONSE = DESCRIPTOR.message_types_by_name['GetPartiesResponse']
_LISTKNOWNPARTIESREQUEST = DESCRIPTOR.message_types_by_name['ListKnownPartiesRequest']
_LISTKNOWNPARTIESRESPONSE = DESCRIPTOR.message_types_by_name['ListKnownPartiesResponse']
_ALLOCATEPARTYREQUEST = DESCRIPTOR.message_types_by_name['AllocatePartyRequest']
_ALLOCATEPARTYRESPONSE = DESCRIPTOR.message_types_by_name['AllocatePartyResponse']
_PARTYDETAILS = DESCRIPTOR.message_types_by_name['PartyDetails']
GetParticipantIdRequest = _reflection.GeneratedProtocolMessageType('GetParticipantIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPARTICIPANTIDREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetParticipantIdRequest)
  })
_sym_db.RegisterMessage(GetParticipantIdRequest)

GetParticipantIdResponse = _reflection.GeneratedProtocolMessageType('GetParticipantIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPARTICIPANTIDRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetParticipantIdResponse)
  })
_sym_db.RegisterMessage(GetParticipantIdResponse)

GetPartiesRequest = _reflection.GeneratedProtocolMessageType('GetPartiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPARTIESREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetPartiesRequest)
  })
_sym_db.RegisterMessage(GetPartiesRequest)

GetPartiesResponse = _reflection.GeneratedProtocolMessageType('GetPartiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPARTIESRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetPartiesResponse)
  })
_sym_db.RegisterMessage(GetPartiesResponse)

ListKnownPartiesRequest = _reflection.GeneratedProtocolMessageType('ListKnownPartiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTKNOWNPARTIESREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.ListKnownPartiesRequest)
  })
_sym_db.RegisterMessage(ListKnownPartiesRequest)

ListKnownPartiesResponse = _reflection.GeneratedProtocolMessageType('ListKnownPartiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTKNOWNPARTIESRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.ListKnownPartiesResponse)
  })
_sym_db.RegisterMessage(ListKnownPartiesResponse)

AllocatePartyRequest = _reflection.GeneratedProtocolMessageType('AllocatePartyRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEPARTYREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.AllocatePartyRequest)
  })
_sym_db.RegisterMessage(AllocatePartyRequest)

AllocatePartyResponse = _reflection.GeneratedProtocolMessageType('AllocatePartyResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEPARTYRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.AllocatePartyResponse)
  })
_sym_db.RegisterMessage(AllocatePartyResponse)

PartyDetails = _reflection.GeneratedProtocolMessageType('PartyDetails', (_message.Message,), {
  'DESCRIPTOR' : _PARTYDETAILS,
  '__module__' : 'com.daml.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.PartyDetails)
  })
_sym_db.RegisterMessage(PartyDetails)

_PARTYMANAGEMENTSERVICE = DESCRIPTOR.services_by_name['PartyManagementService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.daml.ledger.api.v1.adminB PartyManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1/admin\252\002\034Com.Daml.Ledger.Api.V1.Admin'
  _GETPARTICIPANTIDREQUEST._serialized_start=93
  _GETPARTICIPANTIDREQUEST._serialized_end=118
  _GETPARTICIPANTIDRESPONSE._serialized_start=120
  _GETPARTICIPANTIDRESPONSE._serialized_end=185
  _GETPARTIESREQUEST._serialized_start=187
  _GETPARTIESREQUEST._serialized_end=232
  _GETPARTIESRESPONSE._serialized_start=234
  _GETPARTIESRESPONSE._serialized_end=335
  _LISTKNOWNPARTIESREQUEST._serialized_start=337
  _LISTKNOWNPARTIESREQUEST._serialized_end=362
  _LISTKNOWNPARTIESRESPONSE._serialized_start=364
  _LISTKNOWNPARTIESRESPONSE._serialized_end=471
  _ALLOCATEPARTYREQUEST._serialized_start=473
  _ALLOCATEPARTYREQUEST._serialized_end=566
  _ALLOCATEPARTYRESPONSE._serialized_start=568
  _ALLOCATEPARTYRESPONSE._serialized_end=672
  _PARTYDETAILS._serialized_start=674
  _PARTYDETAILS._serialized_end=772
  _PARTYMANAGEMENTSERVICE._serialized_start=775
  _PARTYMANAGEMENTSERVICE._serialized_end=1298
# @@protoc_insertion_point(module_scope)
