// Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.21.12
// source: com/daml/ledger/api/v1/ledger_identity_service.proto

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

// LedgerIdentityServiceClient is the client API for LedgerIdentityService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
//
// Deprecated: Do not use.
type LedgerIdentityServiceClient interface {
	// Deprecated: Do not use.
	// Clients may call this RPC to return the identifier of the ledger they are connected to.
	GetLedgerIdentity(ctx context.Context, in *GetLedgerIdentityRequest, opts ...grpc.CallOption) (*GetLedgerIdentityResponse, error)
}

type ledgerIdentityServiceClient struct {
	cc grpc.ClientConnInterface
}

// Deprecated: Do not use.
func NewLedgerIdentityServiceClient(cc grpc.ClientConnInterface) LedgerIdentityServiceClient {
	return &ledgerIdentityServiceClient{cc}
}

// Deprecated: Do not use.
func (c *ledgerIdentityServiceClient) GetLedgerIdentity(ctx context.Context, in *GetLedgerIdentityRequest, opts ...grpc.CallOption) (*GetLedgerIdentityResponse, error) {
	out := new(GetLedgerIdentityResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.LedgerIdentityService/GetLedgerIdentity", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// LedgerIdentityServiceServer is the server API for LedgerIdentityService service.
// All implementations must embed UnimplementedLedgerIdentityServiceServer
// for forward compatibility
//
// Deprecated: Do not use.
type LedgerIdentityServiceServer interface {
	// Deprecated: Do not use.
	// Clients may call this RPC to return the identifier of the ledger they are connected to.
	GetLedgerIdentity(context.Context, *GetLedgerIdentityRequest) (*GetLedgerIdentityResponse, error)
	mustEmbedUnimplementedLedgerIdentityServiceServer()
}

// UnimplementedLedgerIdentityServiceServer must be embedded to have forward compatible implementations.
type UnimplementedLedgerIdentityServiceServer struct {
}

func (UnimplementedLedgerIdentityServiceServer) GetLedgerIdentity(context.Context, *GetLedgerIdentityRequest) (*GetLedgerIdentityResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetLedgerIdentity not implemented")
}
func (UnimplementedLedgerIdentityServiceServer) mustEmbedUnimplementedLedgerIdentityServiceServer() {}

// UnsafeLedgerIdentityServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to LedgerIdentityServiceServer will
// result in compilation errors.
type UnsafeLedgerIdentityServiceServer interface {
	mustEmbedUnimplementedLedgerIdentityServiceServer()
}

// Deprecated: Do not use.
func RegisterLedgerIdentityServiceServer(s grpc.ServiceRegistrar, srv LedgerIdentityServiceServer) {
	s.RegisterService(&LedgerIdentityService_ServiceDesc, srv)
}

func _LedgerIdentityService_GetLedgerIdentity_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetLedgerIdentityRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LedgerIdentityServiceServer).GetLedgerIdentity(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.LedgerIdentityService/GetLedgerIdentity",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LedgerIdentityServiceServer).GetLedgerIdentity(ctx, req.(*GetLedgerIdentityRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// LedgerIdentityService_ServiceDesc is the grpc.ServiceDesc for LedgerIdentityService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var LedgerIdentityService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.LedgerIdentityService",
	HandlerType: (*LedgerIdentityServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetLedgerIdentity",
			Handler:    _LedgerIdentityService_GetLedgerIdentity_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v1/ledger_identity_service.proto",
}
