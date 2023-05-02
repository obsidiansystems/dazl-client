# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/admin/party_management_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import object_meta_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_object__meta__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;com/daml/ledger/api/v1/admin/party_management_service.proto\x12\x1c\x63om.daml.ledger.api.v1.admin\x1a.com/daml/ledger/api/v1/admin/object_meta.proto\x1a google/protobuf/field_mask.proto\"\x19\n\x17GetParticipantIdRequest\"A\n\x18GetParticipantIdResponse\x12%\n\x0eparticipant_id\x18\x01 \x01(\tR\rparticipantId\"_\n\x11GetPartiesRequest\x12\x18\n\x07parties\x18\x01 \x03(\tR\x07parties\x12\x30\n\x14identity_provider_id\x18\x02 \x01(\tR\x12identityProviderId\"e\n\x12GetPartiesResponse\x12O\n\rparty_details\x18\x01 \x03(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetailsR\x0cpartyDetails\"K\n\x17ListKnownPartiesRequest\x12\x30\n\x14identity_provider_id\x18\x01 \x01(\tR\x12identityProviderId\"k\n\x18ListKnownPartiesResponse\x12O\n\rparty_details\x18\x01 \x03(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetailsR\x0cpartyDetails\"\xe0\x01\n\x14\x41llocatePartyRequest\x12\"\n\rparty_id_hint\x18\x01 \x01(\tR\x0bpartyIdHint\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12O\n\x0elocal_metadata\x18\x03 \x01(\x0b\x32(.com.daml.ledger.api.v1.admin.ObjectMetaR\rlocalMetadata\x12\x30\n\x14identity_provider_id\x18\x04 \x01(\tR\x12identityProviderId\"h\n\x15\x41llocatePartyResponse\x12O\n\rparty_details\x18\x01 \x01(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetailsR\x0cpartyDetails\"\xa9\x01\n\x19UpdatePartyDetailsRequest\x12O\n\rparty_details\x18\x01 \x01(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetailsR\x0cpartyDetails\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"m\n\x1aUpdatePartyDetailsResponse\x12O\n\rparty_details\x18\x01 \x01(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetailsR\x0cpartyDetails\"\xe5\x01\n\x0cPartyDetails\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x19\n\x08is_local\x18\x03 \x01(\x08R\x07isLocal\x12O\n\x0elocal_metadata\x18\x04 \x01(\x0b\x32(.com.daml.ledger.api.v1.admin.ObjectMetaR\rlocalMetadata\x12\x30\n\x14identity_provider_id\x18\x05 \x01(\tR\x12identityProviderId2\x95\x05\n\x16PartyManagementService\x12\x81\x01\n\x10GetParticipantId\x12\x35.com.daml.ledger.api.v1.admin.GetParticipantIdRequest\x1a\x36.com.daml.ledger.api.v1.admin.GetParticipantIdResponse\x12o\n\nGetParties\x12/.com.daml.ledger.api.v1.admin.GetPartiesRequest\x1a\x30.com.daml.ledger.api.v1.admin.GetPartiesResponse\x12\x81\x01\n\x10ListKnownParties\x12\x35.com.daml.ledger.api.v1.admin.ListKnownPartiesRequest\x1a\x36.com.daml.ledger.api.v1.admin.ListKnownPartiesResponse\x12x\n\rAllocateParty\x12\x32.com.daml.ledger.api.v1.admin.AllocatePartyRequest\x1a\x33.com.daml.ledger.api.v1.admin.AllocatePartyResponse\x12\x87\x01\n\x12UpdatePartyDetails\x12\x37.com.daml.ledger.api.v1.admin.UpdatePartyDetailsRequest\x1a\x38.com.daml.ledger.api.v1.admin.UpdatePartyDetailsResponseB\xac\x01\n\x1c\x63om.daml.ledger.api.v1.adminB PartyManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1/admin\xaa\x02\x1c\x43om.Daml.Ledger.Api.V1.Adminb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.admin.party_management_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.daml.ledger.api.v1.adminB PartyManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1/admin\252\002\034Com.Daml.Ledger.Api.V1.Admin'
  _GETPARTICIPANTIDREQUEST._serialized_start=175
  _GETPARTICIPANTIDREQUEST._serialized_end=200
  _GETPARTICIPANTIDRESPONSE._serialized_start=202
  _GETPARTICIPANTIDRESPONSE._serialized_end=267
  _GETPARTIESREQUEST._serialized_start=269
  _GETPARTIESREQUEST._serialized_end=364
  _GETPARTIESRESPONSE._serialized_start=366
  _GETPARTIESRESPONSE._serialized_end=467
  _LISTKNOWNPARTIESREQUEST._serialized_start=469
  _LISTKNOWNPARTIESREQUEST._serialized_end=544
  _LISTKNOWNPARTIESRESPONSE._serialized_start=546
  _LISTKNOWNPARTIESRESPONSE._serialized_end=653
  _ALLOCATEPARTYREQUEST._serialized_start=656
  _ALLOCATEPARTYREQUEST._serialized_end=880
  _ALLOCATEPARTYRESPONSE._serialized_start=882
  _ALLOCATEPARTYRESPONSE._serialized_end=986
  _UPDATEPARTYDETAILSREQUEST._serialized_start=989
  _UPDATEPARTYDETAILSREQUEST._serialized_end=1158
  _UPDATEPARTYDETAILSRESPONSE._serialized_start=1160
  _UPDATEPARTYDETAILSRESPONSE._serialized_end=1269
  _PARTYDETAILS._serialized_start=1272
  _PARTYDETAILS._serialized_end=1501
  _PARTYMANAGEMENTSERVICE._serialized_start=1504
  _PARTYMANAGEMENTSERVICE._serialized_end=2165
# @@protoc_insertion_point(module_scope)
