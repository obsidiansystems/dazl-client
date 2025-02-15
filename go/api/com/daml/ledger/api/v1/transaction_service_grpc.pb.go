// Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.23.4
// source: com/daml/ledger/api/v1/transaction_service.proto

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

// TransactionServiceClient is the client API for TransactionService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TransactionServiceClient interface {
	// Read the ledger's filtered transaction stream for a set of parties.
	// Lists only creates and archives, but not other events.
	// Omits all events on transient contracts, i.e., contracts that were both created and archived in the same transaction.
	GetTransactions(ctx context.Context, in *GetTransactionsRequest, opts ...grpc.CallOption) (TransactionService_GetTransactionsClient, error)
	// Read the ledger's complete transaction tree stream for a set of parties.
	// The stream can be filtered only by parties, but not templates (template filter must be empty).
	GetTransactionTrees(ctx context.Context, in *GetTransactionsRequest, opts ...grpc.CallOption) (TransactionService_GetTransactionTreesClient, error)
	// Lookup a transaction tree by the ID of an event that appears within it.
	// For looking up a transaction instead of a transaction tree, please see GetFlatTransactionByEventId
	GetTransactionByEventId(ctx context.Context, in *GetTransactionByEventIdRequest, opts ...grpc.CallOption) (*GetTransactionResponse, error)
	// Lookup a transaction tree by its ID.
	// For looking up a transaction instead of a transaction tree, please see GetFlatTransactionById
	GetTransactionById(ctx context.Context, in *GetTransactionByIdRequest, opts ...grpc.CallOption) (*GetTransactionResponse, error)
	// Lookup a transaction by the ID of an event that appears within it.
	GetFlatTransactionByEventId(ctx context.Context, in *GetTransactionByEventIdRequest, opts ...grpc.CallOption) (*GetFlatTransactionResponse, error)
	// Lookup a transaction by its ID.
	GetFlatTransactionById(ctx context.Context, in *GetTransactionByIdRequest, opts ...grpc.CallOption) (*GetFlatTransactionResponse, error)
	// Get the current ledger end.
	// Subscriptions started with the returned offset will serve transactions created after this RPC was called.
	GetLedgerEnd(ctx context.Context, in *GetLedgerEndRequest, opts ...grpc.CallOption) (*GetLedgerEndResponse, error)
	// Get the latest successfully pruned ledger offsets
	GetLatestPrunedOffsets(ctx context.Context, in *GetLatestPrunedOffsetsRequest, opts ...grpc.CallOption) (*GetLatestPrunedOffsetsResponse, error)
}

type transactionServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTransactionServiceClient(cc grpc.ClientConnInterface) TransactionServiceClient {
	return &transactionServiceClient{cc}
}

func (c *transactionServiceClient) GetTransactions(ctx context.Context, in *GetTransactionsRequest, opts ...grpc.CallOption) (TransactionService_GetTransactionsClient, error) {
	stream, err := c.cc.NewStream(ctx, &TransactionService_ServiceDesc.Streams[0], "/com.daml.ledger.api.v1.TransactionService/GetTransactions", opts...)
	if err != nil {
		return nil, err
	}
	x := &transactionServiceGetTransactionsClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type TransactionService_GetTransactionsClient interface {
	Recv() (*GetTransactionsResponse, error)
	grpc.ClientStream
}

type transactionServiceGetTransactionsClient struct {
	grpc.ClientStream
}

func (x *transactionServiceGetTransactionsClient) Recv() (*GetTransactionsResponse, error) {
	m := new(GetTransactionsResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *transactionServiceClient) GetTransactionTrees(ctx context.Context, in *GetTransactionsRequest, opts ...grpc.CallOption) (TransactionService_GetTransactionTreesClient, error) {
	stream, err := c.cc.NewStream(ctx, &TransactionService_ServiceDesc.Streams[1], "/com.daml.ledger.api.v1.TransactionService/GetTransactionTrees", opts...)
	if err != nil {
		return nil, err
	}
	x := &transactionServiceGetTransactionTreesClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type TransactionService_GetTransactionTreesClient interface {
	Recv() (*GetTransactionTreesResponse, error)
	grpc.ClientStream
}

type transactionServiceGetTransactionTreesClient struct {
	grpc.ClientStream
}

func (x *transactionServiceGetTransactionTreesClient) Recv() (*GetTransactionTreesResponse, error) {
	m := new(GetTransactionTreesResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *transactionServiceClient) GetTransactionByEventId(ctx context.Context, in *GetTransactionByEventIdRequest, opts ...grpc.CallOption) (*GetTransactionResponse, error) {
	out := new(GetTransactionResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.TransactionService/GetTransactionByEventId", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetTransactionById(ctx context.Context, in *GetTransactionByIdRequest, opts ...grpc.CallOption) (*GetTransactionResponse, error) {
	out := new(GetTransactionResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.TransactionService/GetTransactionById", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetFlatTransactionByEventId(ctx context.Context, in *GetTransactionByEventIdRequest, opts ...grpc.CallOption) (*GetFlatTransactionResponse, error) {
	out := new(GetFlatTransactionResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionByEventId", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetFlatTransactionById(ctx context.Context, in *GetTransactionByIdRequest, opts ...grpc.CallOption) (*GetFlatTransactionResponse, error) {
	out := new(GetFlatTransactionResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionById", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetLedgerEnd(ctx context.Context, in *GetLedgerEndRequest, opts ...grpc.CallOption) (*GetLedgerEndResponse, error) {
	out := new(GetLedgerEndResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.TransactionService/GetLedgerEnd", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetLatestPrunedOffsets(ctx context.Context, in *GetLatestPrunedOffsetsRequest, opts ...grpc.CallOption) (*GetLatestPrunedOffsetsResponse, error) {
	out := new(GetLatestPrunedOffsetsResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.TransactionService/GetLatestPrunedOffsets", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TransactionServiceServer is the server API for TransactionService service.
// All implementations must embed UnimplementedTransactionServiceServer
// for forward compatibility
type TransactionServiceServer interface {
	// Read the ledger's filtered transaction stream for a set of parties.
	// Lists only creates and archives, but not other events.
	// Omits all events on transient contracts, i.e., contracts that were both created and archived in the same transaction.
	GetTransactions(*GetTransactionsRequest, TransactionService_GetTransactionsServer) error
	// Read the ledger's complete transaction tree stream for a set of parties.
	// The stream can be filtered only by parties, but not templates (template filter must be empty).
	GetTransactionTrees(*GetTransactionsRequest, TransactionService_GetTransactionTreesServer) error
	// Lookup a transaction tree by the ID of an event that appears within it.
	// For looking up a transaction instead of a transaction tree, please see GetFlatTransactionByEventId
	GetTransactionByEventId(context.Context, *GetTransactionByEventIdRequest) (*GetTransactionResponse, error)
	// Lookup a transaction tree by its ID.
	// For looking up a transaction instead of a transaction tree, please see GetFlatTransactionById
	GetTransactionById(context.Context, *GetTransactionByIdRequest) (*GetTransactionResponse, error)
	// Lookup a transaction by the ID of an event that appears within it.
	GetFlatTransactionByEventId(context.Context, *GetTransactionByEventIdRequest) (*GetFlatTransactionResponse, error)
	// Lookup a transaction by its ID.
	GetFlatTransactionById(context.Context, *GetTransactionByIdRequest) (*GetFlatTransactionResponse, error)
	// Get the current ledger end.
	// Subscriptions started with the returned offset will serve transactions created after this RPC was called.
	GetLedgerEnd(context.Context, *GetLedgerEndRequest) (*GetLedgerEndResponse, error)
	// Get the latest successfully pruned ledger offsets
	GetLatestPrunedOffsets(context.Context, *GetLatestPrunedOffsetsRequest) (*GetLatestPrunedOffsetsResponse, error)
	mustEmbedUnimplementedTransactionServiceServer()
}

// UnimplementedTransactionServiceServer must be embedded to have forward compatible implementations.
type UnimplementedTransactionServiceServer struct {
}

func (UnimplementedTransactionServiceServer) GetTransactions(*GetTransactionsRequest, TransactionService_GetTransactionsServer) error {
	return status.Errorf(codes.Unimplemented, "method GetTransactions not implemented")
}
func (UnimplementedTransactionServiceServer) GetTransactionTrees(*GetTransactionsRequest, TransactionService_GetTransactionTreesServer) error {
	return status.Errorf(codes.Unimplemented, "method GetTransactionTrees not implemented")
}
func (UnimplementedTransactionServiceServer) GetTransactionByEventId(context.Context, *GetTransactionByEventIdRequest) (*GetTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetTransactionByEventId not implemented")
}
func (UnimplementedTransactionServiceServer) GetTransactionById(context.Context, *GetTransactionByIdRequest) (*GetTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetTransactionById not implemented")
}
func (UnimplementedTransactionServiceServer) GetFlatTransactionByEventId(context.Context, *GetTransactionByEventIdRequest) (*GetFlatTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetFlatTransactionByEventId not implemented")
}
func (UnimplementedTransactionServiceServer) GetFlatTransactionById(context.Context, *GetTransactionByIdRequest) (*GetFlatTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetFlatTransactionById not implemented")
}
func (UnimplementedTransactionServiceServer) GetLedgerEnd(context.Context, *GetLedgerEndRequest) (*GetLedgerEndResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetLedgerEnd not implemented")
}
func (UnimplementedTransactionServiceServer) GetLatestPrunedOffsets(context.Context, *GetLatestPrunedOffsetsRequest) (*GetLatestPrunedOffsetsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetLatestPrunedOffsets not implemented")
}
func (UnimplementedTransactionServiceServer) mustEmbedUnimplementedTransactionServiceServer() {}

// UnsafeTransactionServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TransactionServiceServer will
// result in compilation errors.
type UnsafeTransactionServiceServer interface {
	mustEmbedUnimplementedTransactionServiceServer()
}

func RegisterTransactionServiceServer(s grpc.ServiceRegistrar, srv TransactionServiceServer) {
	s.RegisterService(&TransactionService_ServiceDesc, srv)
}

func _TransactionService_GetTransactions_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(GetTransactionsRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(TransactionServiceServer).GetTransactions(m, &transactionServiceGetTransactionsServer{stream})
}

type TransactionService_GetTransactionsServer interface {
	Send(*GetTransactionsResponse) error
	grpc.ServerStream
}

type transactionServiceGetTransactionsServer struct {
	grpc.ServerStream
}

func (x *transactionServiceGetTransactionsServer) Send(m *GetTransactionsResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _TransactionService_GetTransactionTrees_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(GetTransactionsRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(TransactionServiceServer).GetTransactionTrees(m, &transactionServiceGetTransactionTreesServer{stream})
}

type TransactionService_GetTransactionTreesServer interface {
	Send(*GetTransactionTreesResponse) error
	grpc.ServerStream
}

type transactionServiceGetTransactionTreesServer struct {
	grpc.ServerStream
}

func (x *transactionServiceGetTransactionTreesServer) Send(m *GetTransactionTreesResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _TransactionService_GetTransactionByEventId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTransactionByEventIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetTransactionByEventId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.TransactionService/GetTransactionByEventId",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetTransactionByEventId(ctx, req.(*GetTransactionByEventIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetTransactionById_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTransactionByIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetTransactionById(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.TransactionService/GetTransactionById",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetTransactionById(ctx, req.(*GetTransactionByIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetFlatTransactionByEventId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTransactionByEventIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetFlatTransactionByEventId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionByEventId",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetFlatTransactionByEventId(ctx, req.(*GetTransactionByEventIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetFlatTransactionById_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTransactionByIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetFlatTransactionById(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionById",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetFlatTransactionById(ctx, req.(*GetTransactionByIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetLedgerEnd_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetLedgerEndRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetLedgerEnd(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.TransactionService/GetLedgerEnd",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetLedgerEnd(ctx, req.(*GetLedgerEndRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetLatestPrunedOffsets_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetLatestPrunedOffsetsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetLatestPrunedOffsets(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.TransactionService/GetLatestPrunedOffsets",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetLatestPrunedOffsets(ctx, req.(*GetLatestPrunedOffsetsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TransactionService_ServiceDesc is the grpc.ServiceDesc for TransactionService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TransactionService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.TransactionService",
	HandlerType: (*TransactionServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetTransactionByEventId",
			Handler:    _TransactionService_GetTransactionByEventId_Handler,
		},
		{
			MethodName: "GetTransactionById",
			Handler:    _TransactionService_GetTransactionById_Handler,
		},
		{
			MethodName: "GetFlatTransactionByEventId",
			Handler:    _TransactionService_GetFlatTransactionByEventId_Handler,
		},
		{
			MethodName: "GetFlatTransactionById",
			Handler:    _TransactionService_GetFlatTransactionById_Handler,
		},
		{
			MethodName: "GetLedgerEnd",
			Handler:    _TransactionService_GetLedgerEnd_Handler,
		},
		{
			MethodName: "GetLatestPrunedOffsets",
			Handler:    _TransactionService_GetLatestPrunedOffsets_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "GetTransactions",
			Handler:       _TransactionService_GetTransactions_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "GetTransactionTrees",
			Handler:       _TransactionService_GetTransactionTrees_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "com/daml/ledger/api/v1/transaction_service.proto",
}
