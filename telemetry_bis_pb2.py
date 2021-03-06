# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: telemetry_bis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='telemetry_bis.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\rtelemetry_bis',
  serialized_pb=b'\n\x13telemetry_bis.proto\"\xa8\x02\n\tTelemetry\x12\x15\n\x0bnode_id_str\x18\x01 \x01(\tH\x00\x12\x1d\n\x13subscription_id_str\x18\x03 \x01(\tH\x01\x12\x15\n\rencoding_path\x18\x06 \x01(\t\x12\x15\n\rcollection_id\x18\x08 \x01(\x04\x12\x1d\n\x15\x63ollection_start_time\x18\t \x01(\x04\x12\x15\n\rmsg_timestamp\x18\n \x01(\x04\x12#\n\ndata_gpbkv\x18\x0b \x03(\x0b\x32\x0f.TelemetryField\x12$\n\x08\x64\x61ta_gpb\x18\x0c \x01(\x0b\x32\x12.TelemetryGPBTable\x12\x1b\n\x13\x63ollection_end_time\x18\r \x01(\x04\x42\t\n\x07node_idB\x0e\n\x0csubscription\"\xb7\x02\n\x0eTelemetryField\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\x0b\x62ytes_value\x18\x04 \x01(\x0cH\x00\x12\x16\n\x0cstring_value\x18\x05 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x06 \x01(\x08H\x00\x12\x16\n\x0cuint32_value\x18\x07 \x01(\rH\x00\x12\x16\n\x0cuint64_value\x18\x08 \x01(\x04H\x00\x12\x16\n\x0csint32_value\x18\t \x01(\x11H\x00\x12\x16\n\x0csint64_value\x18\n \x01(\x12H\x00\x12\x16\n\x0c\x64ouble_value\x18\x0b \x01(\x01H\x00\x12\x15\n\x0b\x66loat_value\x18\x0c \x01(\x02H\x00\x12\x1f\n\x06\x66ields\x18\x0f \x03(\x0b\x32\x0f.TelemetryFieldB\x0f\n\rvalue_by_type\"2\n\x11TelemetryGPBTable\x12\x1d\n\x03row\x18\x01 \x03(\x0b\x32\x10.TelemetryRowGPB\"C\n\x0fTelemetryRowGPB\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x0c\n\x04keys\x18\n \x01(\x0c\x12\x0f\n\x07\x63ontent\x18\x0b \x01(\x0c\x42\x0fZ\rtelemetry_bisb\x06proto3'
)




_TELEMETRY = _descriptor.Descriptor(
  name='Telemetry',
  full_name='Telemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id_str', full_name='Telemetry.node_id_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscription_id_str', full_name='Telemetry.subscription_id_str', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding_path', full_name='Telemetry.encoding_path', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_id', full_name='Telemetry.collection_id', index=3,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_start_time', full_name='Telemetry.collection_start_time', index=4,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_timestamp', full_name='Telemetry.msg_timestamp', index=5,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_gpbkv', full_name='Telemetry.data_gpbkv', index=6,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_gpb', full_name='Telemetry.data_gpb', index=7,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_end_time', full_name='Telemetry.collection_end_time', index=8,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='node_id', full_name='Telemetry.node_id',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='subscription', full_name='Telemetry.subscription',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=24,
  serialized_end=320,
)


_TELEMETRYFIELD = _descriptor.Descriptor(
  name='TelemetryField',
  full_name='TelemetryField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='TelemetryField.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='TelemetryField.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='TelemetryField.bytes_value', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='TelemetryField.string_value', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='TelemetryField.bool_value', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32_value', full_name='TelemetryField.uint32_value', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_value', full_name='TelemetryField.uint64_value', index=6,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sint32_value', full_name='TelemetryField.sint32_value', index=7,
      number=9, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sint64_value', full_name='TelemetryField.sint64_value', index=8,
      number=10, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='TelemetryField.double_value', index=9,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='TelemetryField.float_value', index=10,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='TelemetryField.fields', index=11,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value_by_type', full_name='TelemetryField.value_by_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=323,
  serialized_end=634,
)


_TELEMETRYGPBTABLE = _descriptor.Descriptor(
  name='TelemetryGPBTable',
  full_name='TelemetryGPBTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='TelemetryGPBTable.row', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=686,
)


_TELEMETRYROWGPB = _descriptor.Descriptor(
  name='TelemetryRowGPB',
  full_name='TelemetryRowGPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='TelemetryRowGPB.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='TelemetryRowGPB.keys', index=1,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='TelemetryRowGPB.content', index=2,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=688,
  serialized_end=755,
)

_TELEMETRY.fields_by_name['data_gpbkv'].message_type = _TELEMETRYFIELD
_TELEMETRY.fields_by_name['data_gpb'].message_type = _TELEMETRYGPBTABLE
_TELEMETRY.oneofs_by_name['node_id'].fields.append(
  _TELEMETRY.fields_by_name['node_id_str'])
_TELEMETRY.fields_by_name['node_id_str'].containing_oneof = _TELEMETRY.oneofs_by_name['node_id']
_TELEMETRY.oneofs_by_name['subscription'].fields.append(
  _TELEMETRY.fields_by_name['subscription_id_str'])
_TELEMETRY.fields_by_name['subscription_id_str'].containing_oneof = _TELEMETRY.oneofs_by_name['subscription']
_TELEMETRYFIELD.fields_by_name['fields'].message_type = _TELEMETRYFIELD
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['bytes_value'])
_TELEMETRYFIELD.fields_by_name['bytes_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['string_value'])
_TELEMETRYFIELD.fields_by_name['string_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['bool_value'])
_TELEMETRYFIELD.fields_by_name['bool_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['uint32_value'])
_TELEMETRYFIELD.fields_by_name['uint32_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['uint64_value'])
_TELEMETRYFIELD.fields_by_name['uint64_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['sint32_value'])
_TELEMETRYFIELD.fields_by_name['sint32_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['sint64_value'])
_TELEMETRYFIELD.fields_by_name['sint64_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['double_value'])
_TELEMETRYFIELD.fields_by_name['double_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYFIELD.oneofs_by_name['value_by_type'].fields.append(
  _TELEMETRYFIELD.fields_by_name['float_value'])
_TELEMETRYFIELD.fields_by_name['float_value'].containing_oneof = _TELEMETRYFIELD.oneofs_by_name['value_by_type']
_TELEMETRYGPBTABLE.fields_by_name['row'].message_type = _TELEMETRYROWGPB
DESCRIPTOR.message_types_by_name['Telemetry'] = _TELEMETRY
DESCRIPTOR.message_types_by_name['TelemetryField'] = _TELEMETRYFIELD
DESCRIPTOR.message_types_by_name['TelemetryGPBTable'] = _TELEMETRYGPBTABLE
DESCRIPTOR.message_types_by_name['TelemetryRowGPB'] = _TELEMETRYROWGPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Telemetry = _reflection.GeneratedProtocolMessageType('Telemetry', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRY,
  '__module__' : 'telemetry_bis_pb2'
  # @@protoc_insertion_point(class_scope:Telemetry)
  })
_sym_db.RegisterMessage(Telemetry)

TelemetryField = _reflection.GeneratedProtocolMessageType('TelemetryField', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYFIELD,
  '__module__' : 'telemetry_bis_pb2'
  # @@protoc_insertion_point(class_scope:TelemetryField)
  })
_sym_db.RegisterMessage(TelemetryField)

TelemetryGPBTable = _reflection.GeneratedProtocolMessageType('TelemetryGPBTable', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYGPBTABLE,
  '__module__' : 'telemetry_bis_pb2'
  # @@protoc_insertion_point(class_scope:TelemetryGPBTable)
  })
_sym_db.RegisterMessage(TelemetryGPBTable)

TelemetryRowGPB = _reflection.GeneratedProtocolMessageType('TelemetryRowGPB', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYROWGPB,
  '__module__' : 'telemetry_bis_pb2'
  # @@protoc_insertion_point(class_scope:TelemetryRowGPB)
  })
_sym_db.RegisterMessage(TelemetryRowGPB)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
