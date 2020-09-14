// Copyright (c) 2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.25.0
// 	protoc        v3.11.4
// source: com/daml/ledger/api/v1/command_completion_service.proto

package v1

import (
	proto "github.com/golang/protobuf/proto"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
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

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type CompletionStreamRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Must correspond to the ledger id reported by the Ledger Identification Service.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Required
	LedgerId string `protobuf:"bytes,1,opt,name=ledger_id,json=ledgerId,proto3" json:"ledger_id,omitempty"`
	// Only completions of commands submitted with the same application_id will be visible in the stream.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Required
	ApplicationId string `protobuf:"bytes,2,opt,name=application_id,json=applicationId,proto3" json:"application_id,omitempty"`
	// Non-empty list of parties whose data should be included.
	// Must be a valid PartyIdString (as described in ``value.proto``).
	// Required
	Parties []string `protobuf:"bytes,3,rep,name=parties,proto3" json:"parties,omitempty"`
	// This field indicates the minimum offset for completions. This can be used to resume an earlier completion stream.
	// Optional, if not set the ledger uses the current ledger end offset instead.
	Offset *LedgerOffset `protobuf:"bytes,4,opt,name=offset,proto3" json:"offset,omitempty"`
}

func (x *CompletionStreamRequest) Reset() {
	*x = CompletionStreamRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CompletionStreamRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CompletionStreamRequest) ProtoMessage() {}

func (x *CompletionStreamRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CompletionStreamRequest.ProtoReflect.Descriptor instead.
func (*CompletionStreamRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{0}
}

func (x *CompletionStreamRequest) GetLedgerId() string {
	if x != nil {
		return x.LedgerId
	}
	return ""
}

func (x *CompletionStreamRequest) GetApplicationId() string {
	if x != nil {
		return x.ApplicationId
	}
	return ""
}

func (x *CompletionStreamRequest) GetParties() []string {
	if x != nil {
		return x.Parties
	}
	return nil
}

func (x *CompletionStreamRequest) GetOffset() *LedgerOffset {
	if x != nil {
		return x.Offset
	}
	return nil
}

type CompletionStreamResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// This checkpoint may be used to restart consumption.  The
	// checkpoint is after any completions in this response.
	// Optional
	Checkpoint *Checkpoint `protobuf:"bytes,1,opt,name=checkpoint,proto3" json:"checkpoint,omitempty"`
	// If set, one or more completions.
	Completions []*Completion `protobuf:"bytes,2,rep,name=completions,proto3" json:"completions,omitempty"`
}

func (x *CompletionStreamResponse) Reset() {
	*x = CompletionStreamResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CompletionStreamResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CompletionStreamResponse) ProtoMessage() {}

func (x *CompletionStreamResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CompletionStreamResponse.ProtoReflect.Descriptor instead.
func (*CompletionStreamResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{1}
}

func (x *CompletionStreamResponse) GetCheckpoint() *Checkpoint {
	if x != nil {
		return x.Checkpoint
	}
	return nil
}

func (x *CompletionStreamResponse) GetCompletions() []*Completion {
	if x != nil {
		return x.Completions
	}
	return nil
}

// Checkpoints may be used to:
//
// * detect time out of commands.
// * provide an offset which can be used to restart consumption.
type Checkpoint struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// All commands with a maximum record time below this value MUST be considered lost if their completion has not arrived before this checkpoint.
	// Required
	RecordTime *timestamp.Timestamp `protobuf:"bytes,1,opt,name=record_time,json=recordTime,proto3" json:"record_time,omitempty"`
	// May be used in a subsequent CompletionStreamRequest to resume the consumption of this stream at a later time.
	// Required
	Offset *LedgerOffset `protobuf:"bytes,2,opt,name=offset,proto3" json:"offset,omitempty"`
}

func (x *Checkpoint) Reset() {
	*x = Checkpoint{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Checkpoint) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Checkpoint) ProtoMessage() {}

func (x *Checkpoint) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Checkpoint.ProtoReflect.Descriptor instead.
func (*Checkpoint) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{2}
}

func (x *Checkpoint) GetRecordTime() *timestamp.Timestamp {
	if x != nil {
		return x.RecordTime
	}
	return nil
}

func (x *Checkpoint) GetOffset() *LedgerOffset {
	if x != nil {
		return x.Offset
	}
	return nil
}

type CompletionEndRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Must correspond to the ledger ID reported by the Ledger Identification Service.
	// Required
	// Must be a valid LedgerString (as described in ``value.proto``).
	LedgerId string `protobuf:"bytes,1,opt,name=ledger_id,json=ledgerId,proto3" json:"ledger_id,omitempty"`
	// Server side tracing will be registered as a child of the submitted context.
	// This field is a future extension point and is currently not supported.
	// Optional
	TraceContext *TraceContext `protobuf:"bytes,1000,opt,name=trace_context,json=traceContext,proto3" json:"trace_context,omitempty"`
}

func (x *CompletionEndRequest) Reset() {
	*x = CompletionEndRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CompletionEndRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CompletionEndRequest) ProtoMessage() {}

func (x *CompletionEndRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CompletionEndRequest.ProtoReflect.Descriptor instead.
func (*CompletionEndRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{3}
}

func (x *CompletionEndRequest) GetLedgerId() string {
	if x != nil {
		return x.LedgerId
	}
	return ""
}

func (x *CompletionEndRequest) GetTraceContext() *TraceContext {
	if x != nil {
		return x.TraceContext
	}
	return nil
}

type CompletionEndResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// This offset can be used in a CompletionStreamRequest message.
	// Required
	Offset *LedgerOffset `protobuf:"bytes,1,opt,name=offset,proto3" json:"offset,omitempty"`
}

func (x *CompletionEndResponse) Reset() {
	*x = CompletionEndResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CompletionEndResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CompletionEndResponse) ProtoMessage() {}

func (x *CompletionEndResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CompletionEndResponse.ProtoReflect.Descriptor instead.
func (*CompletionEndResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{4}
}

func (x *CompletionEndResponse) GetOffset() *LedgerOffset {
	if x != nil {
		return x.Offset
	}
	return nil
}

var File_com_daml_ledger_api_v1_command_completion_service_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc = []byte{
	0x0a, 0x37, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64,
	0x5f, 0x63, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x73, 0x65, 0x72, 0x76,
	0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x1a, 0x27, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x6f, 0x6d, 0x70, 0x6c, 0x65,
	0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x2a, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x76, 0x31, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x5f, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x2a, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c,
	0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x74,
	0x72, 0x61, 0x63, 0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x74, 0x65, 0x78, 0x74, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x22, 0xb5, 0x01, 0x0a, 0x17, 0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69,
	0x6f, 0x6e, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12,
	0x1b, 0x0a, 0x09, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x08, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x49, 0x64, 0x12, 0x25, 0x0a, 0x0e,
	0x61, 0x70, 0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x0d, 0x61, 0x70, 0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x49, 0x64, 0x12, 0x18, 0x0a, 0x07, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x03,
	0x20, 0x03, 0x28, 0x09, 0x52, 0x07, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x3c, 0x0a,
	0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x4f, 0x66, 0x66,
	0x73, 0x65, 0x74, 0x52, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x22, 0xa4, 0x01, 0x0a, 0x18,
	0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x42, 0x0a, 0x0a, 0x63, 0x68, 0x65, 0x63,
	0x6b, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x70, 0x6f, 0x69, 0x6e, 0x74,
	0x52, 0x0a, 0x63, 0x68, 0x65, 0x63, 0x6b, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x12, 0x44, 0x0a, 0x0b,
	0x63, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28,
	0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x6f, 0x6d, 0x70, 0x6c,
	0x65, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x0b, 0x63, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f,
	0x6e, 0x73, 0x22, 0x87, 0x01, 0x0a, 0x0a, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x70, 0x6f, 0x69, 0x6e,
	0x74, 0x12, 0x3b, 0x0a, 0x0b, 0x72, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x5f, 0x74, 0x69, 0x6d, 0x65,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61,
	0x6d, 0x70, 0x52, 0x0a, 0x72, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x54, 0x69, 0x6d, 0x65, 0x12, 0x3c,
	0x0a, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x4f, 0x66,
	0x66, 0x73, 0x65, 0x74, 0x52, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x22, 0x7f, 0x0a, 0x14,
	0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x45, 0x6e, 0x64, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x12, 0x1b, 0x0a, 0x09, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x5f, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x49,
	0x64, 0x12, 0x4a, 0x0a, 0x0d, 0x74, 0x72, 0x61, 0x63, 0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x74, 0x65,
	0x78, 0x74, 0x18, 0xe8, 0x07, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x31, 0x2e, 0x54, 0x72, 0x61, 0x63, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x65, 0x78, 0x74, 0x52,
	0x0c, 0x74, 0x72, 0x61, 0x63, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x65, 0x78, 0x74, 0x22, 0x55, 0x0a,
	0x15, 0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x45, 0x6e, 0x64, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x3c, 0x0a, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e,
	0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x4f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x52, 0x06, 0x6f, 0x66,
	0x66, 0x73, 0x65, 0x74, 0x32, 0x81, 0x02, 0x0a, 0x18, 0x43, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64,
	0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x12, 0x77, 0x0a, 0x10, 0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x53,
	0x74, 0x72, 0x65, 0x61, 0x6d, 0x12, 0x2f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43,
	0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x30, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e,
	0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x30, 0x01, 0x12, 0x6c, 0x0a, 0x0d, 0x43, 0x6f,
	0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x45, 0x6e, 0x64, 0x12, 0x2c, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x45,
	0x6e, 0x64, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x2d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x31, 0x2e, 0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x45, 0x6e, 0x64,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x42, 0x82, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x31, 0x5a, 0x4f, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61,
	0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x67, 0x6f, 0x2f, 0x76, 0x37, 0x2f,
	0x70, 0x6b, 0x67, 0x2f, 0x67, 0x65, 0x6e, 0x65, 0x72, 0x61, 0x74, 0x65, 0x64, 0x2f, 0x63, 0x6f,
	0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70,
	0x69, 0x2f, 0x76, 0x31, 0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e,
	0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x31, 0x62, 0x06, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescData = file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc
)

func file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescData
}

var file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_com_daml_ledger_api_v1_command_completion_service_proto_goTypes = []interface{}{
	(*CompletionStreamRequest)(nil),  // 0: com.daml.ledger.api.v1.CompletionStreamRequest
	(*CompletionStreamResponse)(nil), // 1: com.daml.ledger.api.v1.CompletionStreamResponse
	(*Checkpoint)(nil),               // 2: com.daml.ledger.api.v1.Checkpoint
	(*CompletionEndRequest)(nil),     // 3: com.daml.ledger.api.v1.CompletionEndRequest
	(*CompletionEndResponse)(nil),    // 4: com.daml.ledger.api.v1.CompletionEndResponse
	(*LedgerOffset)(nil),             // 5: com.daml.ledger.api.v1.LedgerOffset
	(*Completion)(nil),               // 6: com.daml.ledger.api.v1.Completion
	(*timestamp.Timestamp)(nil),      // 7: google.protobuf.Timestamp
	(*TraceContext)(nil),             // 8: com.daml.ledger.api.v1.TraceContext
}
var file_com_daml_ledger_api_v1_command_completion_service_proto_depIdxs = []int32{
	5, // 0: com.daml.ledger.api.v1.CompletionStreamRequest.offset:type_name -> com.daml.ledger.api.v1.LedgerOffset
	2, // 1: com.daml.ledger.api.v1.CompletionStreamResponse.checkpoint:type_name -> com.daml.ledger.api.v1.Checkpoint
	6, // 2: com.daml.ledger.api.v1.CompletionStreamResponse.completions:type_name -> com.daml.ledger.api.v1.Completion
	7, // 3: com.daml.ledger.api.v1.Checkpoint.record_time:type_name -> google.protobuf.Timestamp
	5, // 4: com.daml.ledger.api.v1.Checkpoint.offset:type_name -> com.daml.ledger.api.v1.LedgerOffset
	8, // 5: com.daml.ledger.api.v1.CompletionEndRequest.trace_context:type_name -> com.daml.ledger.api.v1.TraceContext
	5, // 6: com.daml.ledger.api.v1.CompletionEndResponse.offset:type_name -> com.daml.ledger.api.v1.LedgerOffset
	0, // 7: com.daml.ledger.api.v1.CommandCompletionService.CompletionStream:input_type -> com.daml.ledger.api.v1.CompletionStreamRequest
	3, // 8: com.daml.ledger.api.v1.CommandCompletionService.CompletionEnd:input_type -> com.daml.ledger.api.v1.CompletionEndRequest
	1, // 9: com.daml.ledger.api.v1.CommandCompletionService.CompletionStream:output_type -> com.daml.ledger.api.v1.CompletionStreamResponse
	4, // 10: com.daml.ledger.api.v1.CommandCompletionService.CompletionEnd:output_type -> com.daml.ledger.api.v1.CompletionEndResponse
	9, // [9:11] is the sub-list for method output_type
	7, // [7:9] is the sub-list for method input_type
	7, // [7:7] is the sub-list for extension type_name
	7, // [7:7] is the sub-list for extension extendee
	0, // [0:7] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_command_completion_service_proto_init() }
func file_com_daml_ledger_api_v1_command_completion_service_proto_init() {
	if File_com_daml_ledger_api_v1_command_completion_service_proto != nil {
		return
	}
	file_com_daml_ledger_api_v1_completion_proto_init()
	file_com_daml_ledger_api_v1_ledger_offset_proto_init()
	file_com_daml_ledger_api_v1_trace_context_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CompletionStreamRequest); i {
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
		file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CompletionStreamResponse); i {
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
		file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Checkpoint); i {
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
		file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CompletionEndRequest); i {
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
		file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CompletionEndResponse); i {
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
			RawDescriptor: file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v1_command_completion_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_command_completion_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_command_completion_service_proto = out.File
	file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_command_completion_service_proto_goTypes = nil
	file_com_daml_ledger_api_v1_command_completion_service_proto_depIdxs = nil
}
