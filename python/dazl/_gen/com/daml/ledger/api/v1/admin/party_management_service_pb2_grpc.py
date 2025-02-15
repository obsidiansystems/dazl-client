# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import party_management_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2


class PartyManagementServiceStub(object):
    """This service allows inspecting the party management state of the ledger known to the participant
    and managing the participant-local party metadata.

    The authorization rules for its RPCs are specified on the ``<RpcName>Request``
    messages as boolean expressions over these facts:
    (1) ``HasRight(r)`` denoting whether the authenticated user has right ``r`` and
    (2) ``IsAuthenticatedIdentityProviderAdmin(idp)`` denoting whether ``idp`` is equal to the ``identity_provider_id``
    of the authenticated user and the user has an IdentityProviderAdmin right.

    The fields of request messages (and sub-messages) are marked either as ``Optional`` or ``Required``:
    (1) ``Optional`` denoting the client may leave the field unset when sending a request.
    (2) ``Required`` denoting the client must set the field to a non-default value when sending a request.

    A party details resource is described by the ``PartyDetails`` message,
    A party details resource, once it has been created, can be modified using the ``UpdatePartyDetails`` RPC.
    The only fields that can be modified are those marked as ``Modifiable``.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetParticipantId = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.PartyManagementService/GetParticipantId',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetParticipantIdRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetParticipantIdResponse.FromString,
                )
        self.GetParties = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.PartyManagementService/GetParties',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetPartiesRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetPartiesResponse.FromString,
                )
        self.ListKnownParties = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.PartyManagementService/ListKnownParties',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.ListKnownPartiesRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.ListKnownPartiesResponse.FromString,
                )
        self.AllocateParty = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.PartyManagementService/AllocateParty',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.AllocatePartyRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.AllocatePartyResponse.FromString,
                )
        self.UpdatePartyDetails = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.PartyManagementService/UpdatePartyDetails',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.UpdatePartyDetailsRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.UpdatePartyDetailsResponse.FromString,
                )


class PartyManagementServiceServicer(object):
    """This service allows inspecting the party management state of the ledger known to the participant
    and managing the participant-local party metadata.

    The authorization rules for its RPCs are specified on the ``<RpcName>Request``
    messages as boolean expressions over these facts:
    (1) ``HasRight(r)`` denoting whether the authenticated user has right ``r`` and
    (2) ``IsAuthenticatedIdentityProviderAdmin(idp)`` denoting whether ``idp`` is equal to the ``identity_provider_id``
    of the authenticated user and the user has an IdentityProviderAdmin right.

    The fields of request messages (and sub-messages) are marked either as ``Optional`` or ``Required``:
    (1) ``Optional`` denoting the client may leave the field unset when sending a request.
    (2) ``Required`` denoting the client must set the field to a non-default value when sending a request.

    A party details resource is described by the ``PartyDetails`` message,
    A party details resource, once it has been created, can be modified using the ``UpdatePartyDetails`` RPC.
    The only fields that can be modified are those marked as ``Modifiable``.
    """

    def GetParticipantId(self, request, context):
        """Return the identifier of the participant.
        All horizontally scaled replicas should return the same id.
        daml-on-kv-ledger: returns an identifier supplied on command line at launch time
        canton: returns globally unique identifier of the participant
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParties(self, request, context):
        """Get the party details of the given parties. Only known parties will be
        returned in the list.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListKnownParties(self, request, context):
        """List the parties known by the participant.
        The list returned contains parties whose ledger access is facilitated by
        the participant and the ones maintained elsewhere.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllocateParty(self, request, context):
        """Allocates a new party on a ledger and adds it to the set managed by the participant.
        Caller specifies a party identifier suggestion, the actual identifier
        allocated might be different and is implementation specific.
        Caller can specify party metadata that is stored locally on the participant.
        This call may:
        - Succeed, in which case the actual allocated identifier is visible in
        the response.
        - Respond with a gRPC error
        daml-on-kv-ledger: suggestion's uniqueness is checked by the validators in
        the consensus layer and call rejected if the identifier is already present.
        canton: completely different globally unique identifier is allocated.
        Behind the scenes calls to an internal protocol are made. As that protocol
        is richer than the surface protocol, the arguments take implicit values
        The party identifier suggestion must be a valid party name. Party names are required to be non-empty US-ASCII strings built from letters, digits, space,
        colon, minus and underscore limited to 255 chars
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePartyDetails(self, request, context):
        """Update selected modifiable participant-local attributes of a party details resource.
        Can update the participant's local information for local parties.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PartyManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetParticipantId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetParticipantId,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetParticipantIdRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetParticipantIdResponse.SerializeToString,
            ),
            'GetParties': grpc.unary_unary_rpc_method_handler(
                    servicer.GetParties,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetPartiesRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetPartiesResponse.SerializeToString,
            ),
            'ListKnownParties': grpc.unary_unary_rpc_method_handler(
                    servicer.ListKnownParties,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.ListKnownPartiesRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.ListKnownPartiesResponse.SerializeToString,
            ),
            'AllocateParty': grpc.unary_unary_rpc_method_handler(
                    servicer.AllocateParty,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.AllocatePartyRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.AllocatePartyResponse.SerializeToString,
            ),
            'UpdatePartyDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePartyDetails,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.UpdatePartyDetailsRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.UpdatePartyDetailsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v1.admin.PartyManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PartyManagementService(object):
    """This service allows inspecting the party management state of the ledger known to the participant
    and managing the participant-local party metadata.

    The authorization rules for its RPCs are specified on the ``<RpcName>Request``
    messages as boolean expressions over these facts:
    (1) ``HasRight(r)`` denoting whether the authenticated user has right ``r`` and
    (2) ``IsAuthenticatedIdentityProviderAdmin(idp)`` denoting whether ``idp`` is equal to the ``identity_provider_id``
    of the authenticated user and the user has an IdentityProviderAdmin right.

    The fields of request messages (and sub-messages) are marked either as ``Optional`` or ``Required``:
    (1) ``Optional`` denoting the client may leave the field unset when sending a request.
    (2) ``Required`` denoting the client must set the field to a non-default value when sending a request.

    A party details resource is described by the ``PartyDetails`` message,
    A party details resource, once it has been created, can be modified using the ``UpdatePartyDetails`` RPC.
    The only fields that can be modified are those marked as ``Modifiable``.
    """

    @staticmethod
    def GetParticipantId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.PartyManagementService/GetParticipantId',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetParticipantIdRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetParticipantIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetParties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.PartyManagementService/GetParties',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetPartiesRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.GetPartiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListKnownParties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.PartyManagementService/ListKnownParties',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.ListKnownPartiesRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.ListKnownPartiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllocateParty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.PartyManagementService/AllocateParty',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.AllocatePartyRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.AllocatePartyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePartyDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.PartyManagementService/UpdatePartyDetails',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.UpdatePartyDetailsRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_party__management__service__pb2.UpdatePartyDetailsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
