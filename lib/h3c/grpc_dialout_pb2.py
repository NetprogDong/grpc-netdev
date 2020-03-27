# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_dialout.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_dialout.proto',
  package='grpc_dialout',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x12grpc_dialout.proto\x12\x0cgrpc_dialout\"K\n\nDeviceInfo\x12\x14\n\x0cproducerName\x18\x01 \x02(\t\x12\x12\n\ndeviceName\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65viceModel\x18\x03 \x02(\t\"_\n\nDialoutMsg\x12+\n\tdeviceMsg\x18\x01 \x02(\x0b\x32\x18.grpc_dialout.DeviceInfo\x12\x12\n\nsensorPath\x18\x02 \x02(\t\x12\x10\n\x08jsonData\x18\x03 \x02(\t\"#\n\x0f\x44ialoutResponse\x12\x10\n\x08response\x18\x01 \x02(\t2S\n\x0bGRPCDialout\x12\x44\n\x07\x44ialout\x12\x18.grpc_dialout.DialoutMsg\x1a\x1d.grpc_dialout.DialoutResponse(\x01')
)




_DEVICEINFO = _descriptor.Descriptor(
  name='DeviceInfo',
  full_name='grpc_dialout.DeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='producerName', full_name='grpc_dialout.DeviceInfo.producerName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceName', full_name='grpc_dialout.DeviceInfo.deviceName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceModel', full_name='grpc_dialout.DeviceInfo.deviceModel', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=111,
)


_DIALOUTMSG = _descriptor.Descriptor(
  name='DialoutMsg',
  full_name='grpc_dialout.DialoutMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceMsg', full_name='grpc_dialout.DialoutMsg.deviceMsg', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorPath', full_name='grpc_dialout.DialoutMsg.sensorPath', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jsonData', full_name='grpc_dialout.DialoutMsg.jsonData', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=208,
)


_DIALOUTRESPONSE = _descriptor.Descriptor(
  name='DialoutResponse',
  full_name='grpc_dialout.DialoutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='grpc_dialout.DialoutResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=245,
)

_DIALOUTMSG.fields_by_name['deviceMsg'].message_type = _DEVICEINFO
DESCRIPTOR.message_types_by_name['DeviceInfo'] = _DEVICEINFO
DESCRIPTOR.message_types_by_name['DialoutMsg'] = _DIALOUTMSG
DESCRIPTOR.message_types_by_name['DialoutResponse'] = _DIALOUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFO,
  '__module__' : 'grpc_dialout_pb2'
  # @@protoc_insertion_point(class_scope:grpc_dialout.DeviceInfo)
  })
_sym_db.RegisterMessage(DeviceInfo)

DialoutMsg = _reflection.GeneratedProtocolMessageType('DialoutMsg', (_message.Message,), {
  'DESCRIPTOR' : _DIALOUTMSG,
  '__module__' : 'grpc_dialout_pb2'
  # @@protoc_insertion_point(class_scope:grpc_dialout.DialoutMsg)
  })
_sym_db.RegisterMessage(DialoutMsg)

DialoutResponse = _reflection.GeneratedProtocolMessageType('DialoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _DIALOUTRESPONSE,
  '__module__' : 'grpc_dialout_pb2'
  # @@protoc_insertion_point(class_scope:grpc_dialout.DialoutResponse)
  })
_sym_db.RegisterMessage(DialoutResponse)



_GRPCDIALOUT = _descriptor.ServiceDescriptor(
  name='GRPCDialout',
  full_name='grpc_dialout.GRPCDialout',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=247,
  serialized_end=330,
  methods=[
  _descriptor.MethodDescriptor(
    name='Dialout',
    full_name='grpc_dialout.GRPCDialout.Dialout',
    index=0,
    containing_service=None,
    input_type=_DIALOUTMSG,
    output_type=_DIALOUTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCDIALOUT)

DESCRIPTOR.services_by_name['GRPCDialout'] = _GRPCDIALOUT

# @@protoc_insertion_point(module_scope)
