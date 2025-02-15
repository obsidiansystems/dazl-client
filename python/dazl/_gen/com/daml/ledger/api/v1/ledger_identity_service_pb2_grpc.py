# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import ledger_identity_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2


class LedgerIdentityServiceStub(object):
    """DEPRECATED: This service is now deprecated and ledger identity string is optional for all Ledger API requests.

    Allows clients to verify that the server they are communicating with exposes the ledger they wish to operate on.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLedgerIdentity = channel.unary_unary(
                '/com.daml.ledger.api.v1.LedgerIdentityService/GetLedgerIdentity',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityResponse.FromString,
                )


class LedgerIdentityServiceServicer(object):
    """DEPRECATED: This service is now deprecated and ledger identity string is optional for all Ledger API requests.

    Allows clients to verify that the server they are communicating with exposes the ledger they wish to operate on.
    """

    def GetLedgerIdentity(self, request, context):
        """Clients may call this RPC to return the identifier of the ledger they are connected to.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LedgerIdentityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLedgerIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLedgerIdentity,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v1.LedgerIdentityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LedgerIdentityService(object):
    """DEPRECATED: This service is now deprecated and ledger identity string is optional for all Ledger API requests.

    Allows clients to verify that the server they are communicating with exposes the ledger they wish to operate on.
    """

    @staticmethod
    def GetLedgerIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.LedgerIdentityService/GetLedgerIdentity',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
