# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import command_submission_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_command__submission__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CommandSubmissionServiceStub(object):
    """Allows clients to attempt advancing the ledger's state by submitting commands.
    The final states of their submissions are disclosed by the Command Completion Service.
    The on-ledger effects of their submissions are disclosed by the Transaction Service.

    Commands may fail in 2 distinct manners:

    1. Failure communicated synchronously in the gRPC error of the submission.
    2. Failure communicated asynchronously in a Completion, see ``completion.proto``.

    Note that not only successfully submitted commands MAY produce a completion event. For example, the participant MAY
    choose to produce a completion event for a rejection of a duplicate command.

    Clients that do not receive a successful completion about their submission MUST NOT assume that it was successful.
    Clients SHOULD subscribe to the CompletionStream before starting to submit commands to prevent race conditions.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Submit = channel.unary_unary(
                '/com.daml.ledger.api.v1.CommandSubmissionService/Submit',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_command__submission__service__pb2.SubmitRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class CommandSubmissionServiceServicer(object):
    """Allows clients to attempt advancing the ledger's state by submitting commands.
    The final states of their submissions are disclosed by the Command Completion Service.
    The on-ledger effects of their submissions are disclosed by the Transaction Service.

    Commands may fail in 2 distinct manners:

    1. Failure communicated synchronously in the gRPC error of the submission.
    2. Failure communicated asynchronously in a Completion, see ``completion.proto``.

    Note that not only successfully submitted commands MAY produce a completion event. For example, the participant MAY
    choose to produce a completion event for a rejection of a duplicate command.

    Clients that do not receive a successful completion about their submission MUST NOT assume that it was successful.
    Clients SHOULD subscribe to the CompletionStream before starting to submit commands to prevent race conditions.
    """

    def Submit(self, request, context):
        """Submit a single composite command.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommandSubmissionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Submit': grpc.unary_unary_rpc_method_handler(
                    servicer.Submit,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_command__submission__service__pb2.SubmitRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v1.CommandSubmissionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommandSubmissionService(object):
    """Allows clients to attempt advancing the ledger's state by submitting commands.
    The final states of their submissions are disclosed by the Command Completion Service.
    The on-ledger effects of their submissions are disclosed by the Transaction Service.

    Commands may fail in 2 distinct manners:

    1. Failure communicated synchronously in the gRPC error of the submission.
    2. Failure communicated asynchronously in a Completion, see ``completion.proto``.

    Note that not only successfully submitted commands MAY produce a completion event. For example, the participant MAY
    choose to produce a completion event for a rejection of a duplicate command.

    Clients that do not receive a successful completion about their submission MUST NOT assume that it was successful.
    Clients SHOULD subscribe to the CompletionStream before starting to submit commands to prevent race conditions.
    """

    @staticmethod
    def Submit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.CommandSubmissionService/Submit',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_command__submission__service__pb2.SubmitRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
