# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fraud_detection_common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fraud_detection_common.proto',
  package='frauddetection',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x66raud_detection_common.proto\x12\x0e\x66rauddetection\"\xac\x01\n\x16ScoredTransactionState\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x14\n\x0c\x61mount_cents\x18\x04 \x01(\x05\x12\x17\n\x0fpotential_fraud\x18\x05 \x01(\x08\x12\x12\n\nrisk_score\x18\x06 \x01(\x05\x12\x0f\n\x07rule_id\x18\x07 \x01(\t\"\x93\x01\n\x13\x46raudDetectionState\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x0f\n\x07rule_id\x18\x02 \x01(\t\x12\x18\n\x10max_amount_cents\x18\x03 \x01(\x05\x12<\n\x0ctransactions\x18\x04 \x03(\x0b\x32&.frauddetection.ScoredTransactionStateb\x06proto3'
)




_SCOREDTRANSACTIONSTATE = _descriptor.Descriptor(
  name='ScoredTransactionState',
  full_name='frauddetection.ScoredTransactionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='frauddetection.ScoredTransactionState.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='frauddetection.ScoredTransactionState.transaction_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='frauddetection.ScoredTransactionState.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount_cents', full_name='frauddetection.ScoredTransactionState.amount_cents', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='potential_fraud', full_name='frauddetection.ScoredTransactionState.potential_fraud', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='risk_score', full_name='frauddetection.ScoredTransactionState.risk_score', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rule_id', full_name='frauddetection.ScoredTransactionState.rule_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=221,
)


_FRAUDDETECTIONSTATE = _descriptor.Descriptor(
  name='FraudDetectionState',
  full_name='frauddetection.FraudDetectionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='frauddetection.FraudDetectionState.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rule_id', full_name='frauddetection.FraudDetectionState.rule_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_amount_cents', full_name='frauddetection.FraudDetectionState.max_amount_cents', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactions', full_name='frauddetection.FraudDetectionState.transactions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=371,
)

_FRAUDDETECTIONSTATE.fields_by_name['transactions'].message_type = _SCOREDTRANSACTIONSTATE
DESCRIPTOR.message_types_by_name['ScoredTransactionState'] = _SCOREDTRANSACTIONSTATE
DESCRIPTOR.message_types_by_name['FraudDetectionState'] = _FRAUDDETECTIONSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScoredTransactionState = _reflection.GeneratedProtocolMessageType('ScoredTransactionState', (_message.Message,), {
  'DESCRIPTOR' : _SCOREDTRANSACTIONSTATE,
  '__module__' : 'fraud_detection_common_pb2'
  # @@protoc_insertion_point(class_scope:frauddetection.ScoredTransactionState)
  })
_sym_db.RegisterMessage(ScoredTransactionState)

FraudDetectionState = _reflection.GeneratedProtocolMessageType('FraudDetectionState', (_message.Message,), {
  'DESCRIPTOR' : _FRAUDDETECTIONSTATE,
  '__module__' : 'fraud_detection_common_pb2'
  # @@protoc_insertion_point(class_scope:frauddetection.FraudDetectionState)
  })
_sym_db.RegisterMessage(FraudDetectionState)


# @@protoc_insertion_point(module_scope)