// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package v1

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// CommandCompletionServiceClient is the client API for CommandCompletionService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type CommandCompletionServiceClient interface {
	// Subscribe to command completion events.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the request does not include a valid ledger id or if the ledger has been pruned before ``begin``
	// - ``INVALID_ARGUMENT``: if the payload is malformed or is missing required fields
	// - ``OUT_OF_RANGE``: if the absolute offset is not before the end of the ledger
	CompletionStream(ctx context.Context, in *CompletionStreamRequest, opts ...grpc.CallOption) (CommandCompletionService_CompletionStreamClient, error)
	// Returns the offset after the latest completion.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the request does not include a valid ledger id
	CompletionEnd(ctx context.Context, in *CompletionEndRequest, opts ...grpc.CallOption) (*CompletionEndResponse, error)
}

type commandCompletionServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewCommandCompletionServiceClient(cc grpc.ClientConnInterface) CommandCompletionServiceClient {
	return &commandCompletionServiceClient{cc}
}

func (c *commandCompletionServiceClient) CompletionStream(ctx context.Context, in *CompletionStreamRequest, opts ...grpc.CallOption) (CommandCompletionService_CompletionStreamClient, error) {
	stream, err := c.cc.NewStream(ctx, &CommandCompletionService_ServiceDesc.Streams[0], "/com.daml.ledger.api.v1.CommandCompletionService/CompletionStream", opts...)
	if err != nil {
		return nil, err
	}
	x := &commandCompletionServiceCompletionStreamClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type CommandCompletionService_CompletionStreamClient interface {
	Recv() (*CompletionStreamResponse, error)
	grpc.ClientStream
}

type commandCompletionServiceCompletionStreamClient struct {
	grpc.ClientStream
}

func (x *commandCompletionServiceCompletionStreamClient) Recv() (*CompletionStreamResponse, error) {
	m := new(CompletionStreamResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *commandCompletionServiceClient) CompletionEnd(ctx context.Context, in *CompletionEndRequest, opts ...grpc.CallOption) (*CompletionEndResponse, error) {
	out := new(CompletionEndResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.CommandCompletionService/CompletionEnd", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// CommandCompletionServiceServer is the server API for CommandCompletionService service.
// All implementations must embed UnimplementedCommandCompletionServiceServer
// for forward compatibility
type CommandCompletionServiceServer interface {
	// Subscribe to command completion events.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the request does not include a valid ledger id or if the ledger has been pruned before ``begin``
	// - ``INVALID_ARGUMENT``: if the payload is malformed or is missing required fields
	// - ``OUT_OF_RANGE``: if the absolute offset is not before the end of the ledger
	CompletionStream(*CompletionStreamRequest, CommandCompletionService_CompletionStreamServer) error
	// Returns the offset after the latest completion.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the request does not include a valid ledger id
	CompletionEnd(context.Context, *CompletionEndRequest) (*CompletionEndResponse, error)
	mustEmbedUnimplementedCommandCompletionServiceServer()
}

// UnimplementedCommandCompletionServiceServer must be embedded to have forward compatible implementations.
type UnimplementedCommandCompletionServiceServer struct {
}

func (UnimplementedCommandCompletionServiceServer) CompletionStream(*CompletionStreamRequest, CommandCompletionService_CompletionStreamServer) error {
	return status.Errorf(codes.Unimplemented, "method CompletionStream not implemented")
}
func (UnimplementedCommandCompletionServiceServer) CompletionEnd(context.Context, *CompletionEndRequest) (*CompletionEndResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CompletionEnd not implemented")
}
func (UnimplementedCommandCompletionServiceServer) mustEmbedUnimplementedCommandCompletionServiceServer() {
}

// UnsafeCommandCompletionServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to CommandCompletionServiceServer will
// result in compilation errors.
type UnsafeCommandCompletionServiceServer interface {
	mustEmbedUnimplementedCommandCompletionServiceServer()
}

func RegisterCommandCompletionServiceServer(s grpc.ServiceRegistrar, srv CommandCompletionServiceServer) {
	s.RegisterService(&CommandCompletionService_ServiceDesc, srv)
}

func _CommandCompletionService_CompletionStream_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(CompletionStreamRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(CommandCompletionServiceServer).CompletionStream(m, &commandCompletionServiceCompletionStreamServer{stream})
}

type CommandCompletionService_CompletionStreamServer interface {
	Send(*CompletionStreamResponse) error
	grpc.ServerStream
}

type commandCompletionServiceCompletionStreamServer struct {
	grpc.ServerStream
}

func (x *commandCompletionServiceCompletionStreamServer) Send(m *CompletionStreamResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _CommandCompletionService_CompletionEnd_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CompletionEndRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CommandCompletionServiceServer).CompletionEnd(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.CommandCompletionService/CompletionEnd",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CommandCompletionServiceServer).CompletionEnd(ctx, req.(*CompletionEndRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// CommandCompletionService_ServiceDesc is the grpc.ServiceDesc for CommandCompletionService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var CommandCompletionService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.CommandCompletionService",
	HandlerType: (*CommandCompletionServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CompletionEnd",
			Handler:    _CommandCompletionService_CompletionEnd_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "CompletionStream",
			Handler:       _CommandCompletionService_CompletionStream_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "com/daml/ledger/api/v1/command_completion_service.proto",
}
