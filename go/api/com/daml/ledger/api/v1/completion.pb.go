// Copyright (c) 2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.18.1
// source: com/daml/ledger/api/v1/completion.proto

package v1

import (
	status "google.golang.org/genproto/googleapis/rpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	durationpb "google.golang.org/protobuf/types/known/durationpb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// A completion represents the status of a submitted command on the ledger: it can be successful or failed.
type Completion struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The ID of the succeeded or failed command.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Required
	CommandId string `protobuf:"bytes,1,opt,name=command_id,json=commandId,proto3" json:"command_id,omitempty"`
	// Identifies the exact type of the error.
	// For example, malformed or double spend transactions will result in a ``INVALID_ARGUMENT`` status.
	// Transactions with invalid time time windows (which may be valid at a later date) will result in an ``ABORTED`` error.
	// Optional
	Status *status.Status `protobuf:"bytes,2,opt,name=status,proto3" json:"status,omitempty"`
	// The transaction_id of the transaction that resulted from the command with command_id.
	// Only set for successfully executed commands.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Optional
	TransactionId string `protobuf:"bytes,3,opt,name=transaction_id,json=transactionId,proto3" json:"transaction_id,omitempty"`
	// The application-id or user-id that was used for the submission, as described in ``commands.proto``.
	// Must be a valid ApplicationIdString (as described in ``value.proto``).
	// Optional for historic completions where this data is not available.
	ApplicationId string `protobuf:"bytes,4,opt,name=application_id,json=applicationId,proto3" json:"application_id,omitempty"`
	// The set of parties on whose behalf the commands were executed.
	// Contains the union of ``party`` and ``act_as`` from ``commands.proto``.
	// The order of the parties need not be the same as in the submission.
	// Each element must be a valid PartyIdString (as described in ``value.proto``).
	// Optional for historic completions where this data is not available.
	ActAs []string `protobuf:"bytes,5,rep,name=act_as,json=actAs,proto3" json:"act_as,omitempty"`
	// The submission ID this completion refers to, as described in ``commands.proto``.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Optional
	SubmissionId string `protobuf:"bytes,6,opt,name=submission_id,json=submissionId,proto3" json:"submission_id,omitempty"`
	// The actual deduplication window used for the submission, which is derived from
	// ``Commands.deduplication_period``. The ledger may convert the deduplication period into other
	// descriptions and extend the period in implementation-specified ways.
	//
	// Used to audit the deduplication guarantee described in ``commands.proto``.
	//
	// Optional; the deduplication guarantee applies even if the completion omits this field.
	//
	// Types that are assignable to DeduplicationPeriod:
	//	*Completion_DeduplicationOffset
	//	*Completion_DeduplicationDuration
	DeduplicationPeriod isCompletion_DeduplicationPeriod `protobuf_oneof:"deduplication_period"`
}

func (x *Completion) Reset() {
	*x = Completion{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_completion_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Completion) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Completion) ProtoMessage() {}

func (x *Completion) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_completion_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Completion.ProtoReflect.Descriptor instead.
func (*Completion) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_completion_proto_rawDescGZIP(), []int{0}
}

func (x *Completion) GetCommandId() string {
	if x != nil {
		return x.CommandId
	}
	return ""
}

func (x *Completion) GetStatus() *status.Status {
	if x != nil {
		return x.Status
	}
	return nil
}

func (x *Completion) GetTransactionId() string {
	if x != nil {
		return x.TransactionId
	}
	return ""
}

func (x *Completion) GetApplicationId() string {
	if x != nil {
		return x.ApplicationId
	}
	return ""
}

func (x *Completion) GetActAs() []string {
	if x != nil {
		return x.ActAs
	}
	return nil
}

func (x *Completion) GetSubmissionId() string {
	if x != nil {
		return x.SubmissionId
	}
	return ""
}

func (m *Completion) GetDeduplicationPeriod() isCompletion_DeduplicationPeriod {
	if m != nil {
		return m.DeduplicationPeriod
	}
	return nil
}

func (x *Completion) GetDeduplicationOffset() string {
	if x, ok := x.GetDeduplicationPeriod().(*Completion_DeduplicationOffset); ok {
		return x.DeduplicationOffset
	}
	return ""
}

func (x *Completion) GetDeduplicationDuration() *durationpb.Duration {
	if x, ok := x.GetDeduplicationPeriod().(*Completion_DeduplicationDuration); ok {
		return x.DeduplicationDuration
	}
	return nil
}

type isCompletion_DeduplicationPeriod interface {
	isCompletion_DeduplicationPeriod()
}

type Completion_DeduplicationOffset struct {
	// Specifies the start of the deduplication period by a completion stream offset.
	//
	// Must be a valid LedgerString (as described in ``value.proto``).
	DeduplicationOffset string `protobuf:"bytes,8,opt,name=deduplication_offset,json=deduplicationOffset,proto3,oneof"`
}

type Completion_DeduplicationDuration struct {
	// Specifies the length of the deduplication period.
	// It is measured in record time of completions.
	//
	// Must be non-negative.
	DeduplicationDuration *durationpb.Duration `protobuf:"bytes,9,opt,name=deduplication_duration,json=deduplicationDuration,proto3,oneof"`
}

func (*Completion_DeduplicationOffset) isCompletion_DeduplicationPeriod() {}

func (*Completion_DeduplicationDuration) isCompletion_DeduplicationPeriod() {}

var File_com_daml_ledger_api_v1_completion_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_completion_proto_rawDesc = []byte{
	0x0a, 0x27, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74,
	0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x1a, 0x1e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2f, 0x64, 0x75, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x1a, 0x17, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x72, 0x70, 0x63, 0x2f, 0x73, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x99, 0x03, 0x0a, 0x0a, 0x43,
	0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x1d, 0x0a, 0x0a, 0x63, 0x6f, 0x6d,
	0x6d, 0x61, 0x6e, 0x64, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63,
	0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x49, 0x64, 0x12, 0x2a, 0x0a, 0x06, 0x73, 0x74, 0x61, 0x74,
	0x75, 0x73, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x12, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x72, 0x70, 0x63, 0x2e, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x06, 0x73, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x12, 0x25, 0x0a, 0x0e, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74,
	0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0d, 0x74, 0x72,
	0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x49, 0x64, 0x12, 0x25, 0x0a, 0x0e, 0x61,
	0x70, 0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0d, 0x61, 0x70, 0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e,
	0x49, 0x64, 0x12, 0x15, 0x0a, 0x06, 0x61, 0x63, 0x74, 0x5f, 0x61, 0x73, 0x18, 0x05, 0x20, 0x03,
	0x28, 0x09, 0x52, 0x05, 0x61, 0x63, 0x74, 0x41, 0x73, 0x12, 0x23, 0x0a, 0x0d, 0x73, 0x75, 0x62,
	0x6d, 0x69, 0x73, 0x73, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x0c, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x73, 0x73, 0x69, 0x6f, 0x6e, 0x49, 0x64, 0x12, 0x33,
	0x0a, 0x14, 0x64, 0x65, 0x64, 0x75, 0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f,
	0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x18, 0x08, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x13,
	0x64, 0x65, 0x64, 0x75, 0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x4f, 0x66, 0x66,
	0x73, 0x65, 0x74, 0x12, 0x52, 0x0a, 0x16, 0x64, 0x65, 0x64, 0x75, 0x70, 0x6c, 0x69, 0x63, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x64, 0x75, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x09, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x19, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x44, 0x75, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x48, 0x00,
	0x52, 0x15, 0x64, 0x65, 0x64, 0x75, 0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x44,
	0x75, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x42, 0x16, 0x0a, 0x14, 0x64, 0x65, 0x64, 0x75, 0x70,
	0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x70, 0x65, 0x72, 0x69, 0x6f, 0x64, 0x4a,
	0x04, 0x08, 0x07, 0x10, 0x08, 0x52, 0x0f, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x73, 0x73, 0x69, 0x6f,
	0x6e, 0x5f, 0x72, 0x61, 0x6e, 0x6b, 0x42, 0x8e, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x42, 0x14, 0x43, 0x6f, 0x6d, 0x70, 0x6c, 0x65, 0x74, 0x69, 0x6f, 0x6e, 0x4f, 0x75, 0x74,
	0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e,
	0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x37,
	0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c,
	0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0xaa, 0x02,
	0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_completion_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_completion_proto_rawDescData = file_com_daml_ledger_api_v1_completion_proto_rawDesc
)

func file_com_daml_ledger_api_v1_completion_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_completion_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_completion_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_completion_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_completion_proto_rawDescData
}

var file_com_daml_ledger_api_v1_completion_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_com_daml_ledger_api_v1_completion_proto_goTypes = []interface{}{
	(*Completion)(nil),          // 0: com.daml.ledger.api.v1.Completion
	(*status.Status)(nil),       // 1: google.rpc.Status
	(*durationpb.Duration)(nil), // 2: google.protobuf.Duration
}
var file_com_daml_ledger_api_v1_completion_proto_depIdxs = []int32{
	1, // 0: com.daml.ledger.api.v1.Completion.status:type_name -> google.rpc.Status
	2, // 1: com.daml.ledger.api.v1.Completion.deduplication_duration:type_name -> google.protobuf.Duration
	2, // [2:2] is the sub-list for method output_type
	2, // [2:2] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_completion_proto_init() }
func file_com_daml_ledger_api_v1_completion_proto_init() {
	if File_com_daml_ledger_api_v1_completion_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_completion_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Completion); i {
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
	file_com_daml_ledger_api_v1_completion_proto_msgTypes[0].OneofWrappers = []interface{}{
		(*Completion_DeduplicationOffset)(nil),
		(*Completion_DeduplicationDuration)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v1_completion_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v1_completion_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_completion_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_completion_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_completion_proto = out.File
	file_com_daml_ledger_api_v1_completion_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_completion_proto_goTypes = nil
	file_com_daml_ledger_api_v1_completion_proto_depIdxs = nil
}
