// Copyright (c) 2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v4.23.4
// source: com/daml/ledger/api/v1/transaction.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// Complete view of an on-ledger transaction.
type TransactionTree struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Assigned by the server. Useful for correlating logs.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Required
	TransactionId string `protobuf:"bytes,1,opt,name=transaction_id,json=transactionId,proto3" json:"transaction_id,omitempty"`
	// The ID of the command which resulted in this transaction. Missing for everyone except the submitting party.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Optional
	CommandId string `protobuf:"bytes,2,opt,name=command_id,json=commandId,proto3" json:"command_id,omitempty"`
	// The workflow ID used in command submission. Only set if the ``workflow_id`` for the command was set.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Optional
	WorkflowId string `protobuf:"bytes,3,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"`
	// Ledger effective time.
	// Required
	EffectiveAt *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=effective_at,json=effectiveAt,proto3" json:"effective_at,omitempty"`
	// The absolute offset. The format of this field is described in ``ledger_offset.proto``.
	// Required
	Offset string `protobuf:"bytes,6,opt,name=offset,proto3" json:"offset,omitempty"`
	// Changes to the ledger that were caused by this transaction. Nodes of the transaction tree.
	// Each key be a valid LedgerString (as describe in ``value.proto``).
	// Required
	EventsById map[string]*TreeEvent `protobuf:"bytes,7,rep,name=events_by_id,json=eventsById,proto3" json:"events_by_id,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	// Roots of the transaction tree.
	// Each element must be a valid LedgerString (as describe in ``value.proto``).
	// The elements are in the same order as the commands in the
	// corresponding Commands object that triggered this transaction.
	// Required
	RootEventIds []string `protobuf:"bytes,8,rep,name=root_event_ids,json=rootEventIds,proto3" json:"root_event_ids,omitempty"`
}

func (x *TransactionTree) Reset() {
	*x = TransactionTree{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_transaction_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransactionTree) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransactionTree) ProtoMessage() {}

func (x *TransactionTree) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransactionTree.ProtoReflect.Descriptor instead.
func (*TransactionTree) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_transaction_proto_rawDescGZIP(), []int{0}
}

func (x *TransactionTree) GetTransactionId() string {
	if x != nil {
		return x.TransactionId
	}
	return ""
}

func (x *TransactionTree) GetCommandId() string {
	if x != nil {
		return x.CommandId
	}
	return ""
}

func (x *TransactionTree) GetWorkflowId() string {
	if x != nil {
		return x.WorkflowId
	}
	return ""
}

func (x *TransactionTree) GetEffectiveAt() *timestamppb.Timestamp {
	if x != nil {
		return x.EffectiveAt
	}
	return nil
}

func (x *TransactionTree) GetOffset() string {
	if x != nil {
		return x.Offset
	}
	return ""
}

func (x *TransactionTree) GetEventsById() map[string]*TreeEvent {
	if x != nil {
		return x.EventsById
	}
	return nil
}

func (x *TransactionTree) GetRootEventIds() []string {
	if x != nil {
		return x.RootEventIds
	}
	return nil
}

// Each tree event message type below contains a ``witness_parties`` field which
// indicates the subset of the requested parties that can see the event
// in question.
//
// Note that transaction trees might contain events with
// _no_ witness parties, which were included simply because they were
// children of events which have witnesses.
type TreeEvent struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Kind:
	//	*TreeEvent_Created
	//	*TreeEvent_Exercised
	Kind isTreeEvent_Kind `protobuf_oneof:"kind"`
}

func (x *TreeEvent) Reset() {
	*x = TreeEvent{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_transaction_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TreeEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TreeEvent) ProtoMessage() {}

func (x *TreeEvent) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TreeEvent.ProtoReflect.Descriptor instead.
func (*TreeEvent) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_transaction_proto_rawDescGZIP(), []int{1}
}

func (m *TreeEvent) GetKind() isTreeEvent_Kind {
	if m != nil {
		return m.Kind
	}
	return nil
}

func (x *TreeEvent) GetCreated() *CreatedEvent {
	if x, ok := x.GetKind().(*TreeEvent_Created); ok {
		return x.Created
	}
	return nil
}

func (x *TreeEvent) GetExercised() *ExercisedEvent {
	if x, ok := x.GetKind().(*TreeEvent_Exercised); ok {
		return x.Exercised
	}
	return nil
}

type isTreeEvent_Kind interface {
	isTreeEvent_Kind()
}

type TreeEvent_Created struct {
	Created *CreatedEvent `protobuf:"bytes,1,opt,name=created,proto3,oneof"`
}

type TreeEvent_Exercised struct {
	Exercised *ExercisedEvent `protobuf:"bytes,2,opt,name=exercised,proto3,oneof"`
}

func (*TreeEvent_Created) isTreeEvent_Kind() {}

func (*TreeEvent_Exercised) isTreeEvent_Kind() {}

// Filtered view of an on-ledger transaction's create and archive events.
type Transaction struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Assigned by the server. Useful for correlating logs.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Required
	TransactionId string `protobuf:"bytes,1,opt,name=transaction_id,json=transactionId,proto3" json:"transaction_id,omitempty"`
	// The ID of the command which resulted in this transaction. Missing for everyone except the submitting party.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Optional
	CommandId string `protobuf:"bytes,2,opt,name=command_id,json=commandId,proto3" json:"command_id,omitempty"`
	// The workflow ID used in command submission.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Optional
	WorkflowId string `protobuf:"bytes,3,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"`
	// Ledger effective time.
	// Must be a valid LedgerString (as described in ``value.proto``).
	// Required
	EffectiveAt *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=effective_at,json=effectiveAt,proto3" json:"effective_at,omitempty"`
	// The collection of events.
	// Only contains ``CreatedEvent`` or ``ArchivedEvent``.
	// Required
	Events []*Event `protobuf:"bytes,5,rep,name=events,proto3" json:"events,omitempty"`
	// The absolute offset. The format of this field is described in ``ledger_offset.proto``.
	// Required
	Offset string `protobuf:"bytes,6,opt,name=offset,proto3" json:"offset,omitempty"`
}

func (x *Transaction) Reset() {
	*x = Transaction{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_transaction_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Transaction) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Transaction) ProtoMessage() {}

func (x *Transaction) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Transaction.ProtoReflect.Descriptor instead.
func (*Transaction) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_transaction_proto_rawDescGZIP(), []int{2}
}

func (x *Transaction) GetTransactionId() string {
	if x != nil {
		return x.TransactionId
	}
	return ""
}

func (x *Transaction) GetCommandId() string {
	if x != nil {
		return x.CommandId
	}
	return ""
}

func (x *Transaction) GetWorkflowId() string {
	if x != nil {
		return x.WorkflowId
	}
	return ""
}

func (x *Transaction) GetEffectiveAt() *timestamppb.Timestamp {
	if x != nil {
		return x.EffectiveAt
	}
	return nil
}

func (x *Transaction) GetEvents() []*Event {
	if x != nil {
		return x.Events
	}
	return nil
}

func (x *Transaction) GetOffset() string {
	if x != nil {
		return x.Offset
	}
	return ""
}

var File_com_daml_ledger_api_v1_transaction_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_transaction_proto_rawDesc = []byte{
	0x0a, 0x28, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63,
	0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x31, 0x1a, 0x22, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xb8, 0x03, 0x0a, 0x0f, 0x54, 0x72, 0x61, 0x6e,
	0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x72, 0x65, 0x65, 0x12, 0x25, 0x0a, 0x0e, 0x74,
	0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0d, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e,
	0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x5f, 0x69, 0x64,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x49,
	0x64, 0x12, 0x1f, 0x0a, 0x0b, 0x77, 0x6f, 0x72, 0x6b, 0x66, 0x6c, 0x6f, 0x77, 0x5f, 0x69, 0x64,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x77, 0x6f, 0x72, 0x6b, 0x66, 0x6c, 0x6f, 0x77,
	0x49, 0x64, 0x12, 0x3d, 0x0a, 0x0c, 0x65, 0x66, 0x66, 0x65, 0x63, 0x74, 0x69, 0x76, 0x65, 0x5f,
	0x61, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x52, 0x0b, 0x65, 0x66, 0x66, 0x65, 0x63, 0x74, 0x69, 0x76, 0x65, 0x41,
	0x74, 0x12, 0x16, 0x0a, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x18, 0x06, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x12, 0x59, 0x0a, 0x0c, 0x65, 0x76, 0x65,
	0x6e, 0x74, 0x73, 0x5f, 0x62, 0x79, 0x5f, 0x69, 0x64, 0x18, 0x07, 0x20, 0x03, 0x28, 0x0b, 0x32,
	0x37, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63,
	0x74, 0x69, 0x6f, 0x6e, 0x54, 0x72, 0x65, 0x65, 0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x42,
	0x79, 0x49, 0x64, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x0a, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73,
	0x42, 0x79, 0x49, 0x64, 0x12, 0x24, 0x0a, 0x0e, 0x72, 0x6f, 0x6f, 0x74, 0x5f, 0x65, 0x76, 0x65,
	0x6e, 0x74, 0x5f, 0x69, 0x64, 0x73, 0x18, 0x08, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0c, 0x72, 0x6f,
	0x6f, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x49, 0x64, 0x73, 0x1a, 0x60, 0x0a, 0x0f, 0x45, 0x76,
	0x65, 0x6e, 0x74, 0x73, 0x42, 0x79, 0x49, 0x64, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a,
	0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12,
	0x37, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x21,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x54, 0x72, 0x65, 0x65, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x4a, 0x04, 0x08, 0x05,
	0x10, 0x06, 0x22, 0x9d, 0x01, 0x0a, 0x09, 0x54, 0x72, 0x65, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74,
	0x12, 0x40, 0x0a, 0x07, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x48, 0x00, 0x52, 0x07, 0x63, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x64, 0x12, 0x46, 0x0a, 0x09, 0x65, 0x78, 0x65, 0x72, 0x63, 0x69, 0x73, 0x65, 0x64, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x26, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x45,
	0x78, 0x65, 0x72, 0x63, 0x69, 0x73, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x48, 0x00, 0x52,
	0x09, 0x65, 0x78, 0x65, 0x72, 0x63, 0x69, 0x73, 0x65, 0x64, 0x42, 0x06, 0x0a, 0x04, 0x6b, 0x69,
	0x6e, 0x64, 0x22, 0x82, 0x02, 0x0a, 0x0b, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69,
	0x6f, 0x6e, 0x12, 0x25, 0x0a, 0x0e, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f,
	0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0d, 0x74, 0x72, 0x61, 0x6e,
	0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x63, 0x6f, 0x6d,
	0x6d, 0x61, 0x6e, 0x64, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63,
	0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x49, 0x64, 0x12, 0x1f, 0x0a, 0x0b, 0x77, 0x6f, 0x72, 0x6b,
	0x66, 0x6c, 0x6f, 0x77, 0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x77,
	0x6f, 0x72, 0x6b, 0x66, 0x6c, 0x6f, 0x77, 0x49, 0x64, 0x12, 0x3d, 0x0a, 0x0c, 0x65, 0x66, 0x66,
	0x65, 0x63, 0x74, 0x69, 0x76, 0x65, 0x5f, 0x61, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75,
	0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x0b, 0x65, 0x66, 0x66,
	0x65, 0x63, 0x74, 0x69, 0x76, 0x65, 0x41, 0x74, 0x12, 0x35, 0x0a, 0x06, 0x65, 0x76, 0x65, 0x6e,
	0x74, 0x73, 0x18, 0x05, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x06, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x12,
	0x16, 0x0a, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x42, 0x8f, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x31, 0x42, 0x15, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x4f,
	0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68, 0x75,
	0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f,
	0x76, 0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61,
	0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31,
	0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x33,
}

var (
	file_com_daml_ledger_api_v1_transaction_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_transaction_proto_rawDescData = file_com_daml_ledger_api_v1_transaction_proto_rawDesc
)

func file_com_daml_ledger_api_v1_transaction_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_transaction_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_transaction_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_transaction_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_transaction_proto_rawDescData
}

var file_com_daml_ledger_api_v1_transaction_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_daml_ledger_api_v1_transaction_proto_goTypes = []interface{}{
	(*TransactionTree)(nil),       // 0: com.daml.ledger.api.v1.TransactionTree
	(*TreeEvent)(nil),             // 1: com.daml.ledger.api.v1.TreeEvent
	(*Transaction)(nil),           // 2: com.daml.ledger.api.v1.Transaction
	nil,                           // 3: com.daml.ledger.api.v1.TransactionTree.EventsByIdEntry
	(*timestamppb.Timestamp)(nil), // 4: google.protobuf.Timestamp
	(*CreatedEvent)(nil),          // 5: com.daml.ledger.api.v1.CreatedEvent
	(*ExercisedEvent)(nil),        // 6: com.daml.ledger.api.v1.ExercisedEvent
	(*Event)(nil),                 // 7: com.daml.ledger.api.v1.Event
}
var file_com_daml_ledger_api_v1_transaction_proto_depIdxs = []int32{
	4, // 0: com.daml.ledger.api.v1.TransactionTree.effective_at:type_name -> google.protobuf.Timestamp
	3, // 1: com.daml.ledger.api.v1.TransactionTree.events_by_id:type_name -> com.daml.ledger.api.v1.TransactionTree.EventsByIdEntry
	5, // 2: com.daml.ledger.api.v1.TreeEvent.created:type_name -> com.daml.ledger.api.v1.CreatedEvent
	6, // 3: com.daml.ledger.api.v1.TreeEvent.exercised:type_name -> com.daml.ledger.api.v1.ExercisedEvent
	4, // 4: com.daml.ledger.api.v1.Transaction.effective_at:type_name -> google.protobuf.Timestamp
	7, // 5: com.daml.ledger.api.v1.Transaction.events:type_name -> com.daml.ledger.api.v1.Event
	1, // 6: com.daml.ledger.api.v1.TransactionTree.EventsByIdEntry.value:type_name -> com.daml.ledger.api.v1.TreeEvent
	7, // [7:7] is the sub-list for method output_type
	7, // [7:7] is the sub-list for method input_type
	7, // [7:7] is the sub-list for extension type_name
	7, // [7:7] is the sub-list for extension extendee
	0, // [0:7] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_transaction_proto_init() }
func file_com_daml_ledger_api_v1_transaction_proto_init() {
	if File_com_daml_ledger_api_v1_transaction_proto != nil {
		return
	}
	file_com_daml_ledger_api_v1_event_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_transaction_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransactionTree); i {
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
		file_com_daml_ledger_api_v1_transaction_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TreeEvent); i {
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
		file_com_daml_ledger_api_v1_transaction_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Transaction); i {
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
	file_com_daml_ledger_api_v1_transaction_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*TreeEvent_Created)(nil),
		(*TreeEvent_Exercised)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v1_transaction_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v1_transaction_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_transaction_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_transaction_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_transaction_proto = out.File
	file_com_daml_ledger_api_v1_transaction_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_transaction_proto_goTypes = nil
	file_com_daml_ledger_api_v1_transaction_proto_depIdxs = nil
}
