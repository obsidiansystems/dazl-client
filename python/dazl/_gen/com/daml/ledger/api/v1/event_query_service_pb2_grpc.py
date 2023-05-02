# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import event_query_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2


class EventQueryServiceStub(object):
    """Query events by contract id or key.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEventsByContractId = channel.unary_unary(
                '/com.daml.ledger.api.v1.EventQueryService/GetEventsByContractId',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractIdRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractIdResponse.FromString,
                )
        self.GetEventsByContractKey = channel.unary_unary(
                '/com.daml.ledger.api.v1.EventQueryService/GetEventsByContractKey',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractKeyRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractKeyResponse.FromString,
                )


class EventQueryServiceServicer(object):
    """Query events by contract id or key.
    """

    def GetEventsByContractId(self, request, context):
        """Get the create and the consuming exercise event for the contract with the provided ID.
        No events will be returned for contracts that have been pruned because they 
        have already been archived before the latest pruning offset. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEventsByContractKey(self, request, context):
        """Get all create and consuming exercise events for the contracts with the provided contract key.
        Only events for unpruned contracts will be returned.
        Matching events are delivered in reverse chronological order, i.e.,
        the most recent events are delivered first.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventQueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEventsByContractId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEventsByContractId,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractIdRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractIdResponse.SerializeToString,
            ),
            'GetEventsByContractKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEventsByContractKey,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractKeyRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractKeyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v1.EventQueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventQueryService(object):
    """Query events by contract id or key.
    """

    @staticmethod
    def GetEventsByContractId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.EventQueryService/GetEventsByContractId',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractIdRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEventsByContractKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.EventQueryService/GetEventsByContractKey',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractKeyRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__query__service__pb2.GetEventsByContractKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
