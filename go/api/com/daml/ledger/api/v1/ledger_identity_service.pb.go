// Copyright (c) 2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.19.4
// source: com/daml/ledger/api/v1/ledger_identity_service.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// Deprecated: Do not use.
type GetLedgerIdentityRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *GetLedgerIdentityRequest) Reset() {
	*x = GetLedgerIdentityRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_ledger_identity_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetLedgerIdentityRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetLedgerIdentityRequest) ProtoMessage() {}

func (x *GetLedgerIdentityRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_ledger_identity_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetLedgerIdentityRequest.ProtoReflect.Descriptor instead.
func (*GetLedgerIdentityRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescGZIP(), []int{0}
}

// Deprecated: Do not use.
type GetLedgerIdentityResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The ID of the ledger exposed by the server.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Optional
	//
	// Deprecated: Do not use.
	LedgerId string `protobuf:"bytes,1,opt,name=ledger_id,json=ledgerId,proto3" json:"ledger_id,omitempty"`
}

func (x *GetLedgerIdentityResponse) Reset() {
	*x = GetLedgerIdentityResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_ledger_identity_service_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetLedgerIdentityResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetLedgerIdentityResponse) ProtoMessage() {}

func (x *GetLedgerIdentityResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_ledger_identity_service_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetLedgerIdentityResponse.ProtoReflect.Descriptor instead.
func (*GetLedgerIdentityResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescGZIP(), []int{1}
}

// Deprecated: Do not use.
func (x *GetLedgerIdentityResponse) GetLedgerId() string {
	if x != nil {
		return x.LedgerId
	}
	return ""
}

var File_com_daml_ledger_api_v1_ledger_identity_service_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDesc = []byte{
	0x0a, 0x34, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x5f,
	0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x22, 0x1e,
	0x0a, 0x18, 0x47, 0x65, 0x74, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x49, 0x64, 0x65, 0x6e, 0x74,
	0x69, 0x74, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x3a, 0x02, 0x18, 0x01, 0x22, 0x40,
	0x0a, 0x19, 0x47, 0x65, 0x74, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x49, 0x64, 0x65, 0x6e, 0x74,
	0x69, 0x74, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x1f, 0x0a, 0x09, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x02,
	0x18, 0x01, 0x52, 0x08, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x49, 0x64, 0x3a, 0x02, 0x18, 0x01,
	0x32, 0x9b, 0x01, 0x0a, 0x15, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x49, 0x64, 0x65, 0x6e, 0x74,
	0x69, 0x74, 0x79, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x7d, 0x0a, 0x11, 0x47, 0x65,
	0x74, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x12,
	0x30, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x4c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x31, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x4c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x22, 0x03, 0x88, 0x02, 0x01, 0x1a, 0x03, 0x88, 0x02, 0x01, 0x42, 0x99,
	0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x42, 0x1f, 0x4c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65,
	0x4f, 0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68,
	0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74,
	0x2f, 0x76, 0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76,
	0x31, 0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescData = file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDesc
)

func file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDescData
}

var file_com_daml_ledger_api_v1_ledger_identity_service_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_daml_ledger_api_v1_ledger_identity_service_proto_goTypes = []interface{}{
	(*GetLedgerIdentityRequest)(nil),  // 0: com.daml.ledger.api.v1.GetLedgerIdentityRequest
	(*GetLedgerIdentityResponse)(nil), // 1: com.daml.ledger.api.v1.GetLedgerIdentityResponse
}
var file_com_daml_ledger_api_v1_ledger_identity_service_proto_depIdxs = []int32{
	0, // 0: com.daml.ledger.api.v1.LedgerIdentityService.GetLedgerIdentity:input_type -> com.daml.ledger.api.v1.GetLedgerIdentityRequest
	1, // 1: com.daml.ledger.api.v1.LedgerIdentityService.GetLedgerIdentity:output_type -> com.daml.ledger.api.v1.GetLedgerIdentityResponse
	1, // [1:2] is the sub-list for method output_type
	0, // [0:1] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_ledger_identity_service_proto_init() }
func file_com_daml_ledger_api_v1_ledger_identity_service_proto_init() {
	if File_com_daml_ledger_api_v1_ledger_identity_service_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_ledger_identity_service_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetLedgerIdentityRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_ledger_identity_service_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetLedgerIdentityResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v1_ledger_identity_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_ledger_identity_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_ledger_identity_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_ledger_identity_service_proto = out.File
	file_com_daml_ledger_api_v1_ledger_identity_service_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_ledger_identity_service_proto_goTypes = nil
	file_com_daml_ledger_api_v1_ledger_identity_service_proto_depIdxs = nil
}
