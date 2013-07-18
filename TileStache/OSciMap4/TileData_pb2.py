# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='TileStache/OSciMap/TileData.proto',
  package='org.oscim.database.oscimap',
  serialized_pb='\n!TileStache/OSciMap/TileData.proto\x12\x1aorg.oscim.database.oscimap\"\xb9\x03\n\x04\x44\x61ta\x12\x10\n\x08num_tags\x18\x01 \x02(\r\x12\x10\n\x04keys\x18\x02 \x03(\rB\x02\x10\x01\x12\x0e\n\x06values\x18\x03 \x03(\t\x12\x37\n\x05lines\x18\x0b \x03(\x0b\x32(.org.oscim.database.oscimap.Data.Element\x12:\n\x08polygons\x18\x0c \x03(\x0b\x32(.org.oscim.database.oscimap.Data.Element\x12\x38\n\x06points\x18\r \x03(\x0b\x32(.org.oscim.database.oscimap.Data.Element\x12:\n\x08waylabel\x18\x15 \x03(\x0b\x32(.org.oscim.database.oscimap.Data.Element\x12\r\n\x05water\x18\x1f \x01(\r\x1a\x82\x01\n\x07\x45lement\x12\x16\n\x0bnum_indices\x18\x01 \x01(\r:\x01\x31\x12\x10\n\x04tags\x18\x0b \x03(\rB\x02\x10\x01\x12\x13\n\x07indices\x18\x0c \x03(\rB\x02\x10\x01\x12\x17\n\x0b\x63oordinates\x18\r \x03(\x11\x42\x02\x10\x01\x12\r\n\x05layer\x18\x15 \x01(\r\x12\x10\n\x08priority\x18\x1f \x01(\r')




_DATA_ELEMENT = descriptor.Descriptor(
  name='Element',
  full_name='org.oscim.database.oscimap.Data.Element',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='num_indices', full_name='org.oscim.database.oscimap.Data.Element.num_indices', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tags', full_name='org.oscim.database.oscimap.Data.Element.tags', index=1,
      number=11, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='indices', full_name='org.oscim.database.oscimap.Data.Element.indices', index=2,
      number=12, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='coordinates', full_name='org.oscim.database.oscimap.Data.Element.coordinates', index=3,
      number=13, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='layer', full_name='org.oscim.database.oscimap.Data.Element.layer', index=4,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='priority', full_name='org.oscim.database.oscimap.Data.Element.priority', index=5,
      number=31, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=377,
  serialized_end=507,
)

_DATA = descriptor.Descriptor(
  name='Data',
  full_name='org.oscim.database.oscimap.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='num_tags', full_name='org.oscim.database.oscimap.Data.num_tags', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keys', full_name='org.oscim.database.oscimap.Data.keys', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='values', full_name='org.oscim.database.oscimap.Data.values', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lines', full_name='org.oscim.database.oscimap.Data.lines', index=3,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='polygons', full_name='org.oscim.database.oscimap.Data.polygons', index=4,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='points', full_name='org.oscim.database.oscimap.Data.points', index=5,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='waylabel', full_name='org.oscim.database.oscimap.Data.waylabel', index=6,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='water', full_name='org.oscim.database.oscimap.Data.water', index=7,
      number=31, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DATA_ELEMENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=66,
  serialized_end=507,
)

_DATA_ELEMENT.containing_type = _DATA;
_DATA.fields_by_name['lines'].message_type = _DATA_ELEMENT
_DATA.fields_by_name['polygons'].message_type = _DATA_ELEMENT
_DATA.fields_by_name['points'].message_type = _DATA_ELEMENT
_DATA.fields_by_name['waylabel'].message_type = _DATA_ELEMENT
DESCRIPTOR.message_types_by_name['Data'] = _DATA

class Data(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Element(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _DATA_ELEMENT
    
    # @@protoc_insertion_point(class_scope:org.oscim.database.oscimap.Data.Element)
  DESCRIPTOR = _DATA
  
  # @@protoc_insertion_point(class_scope:org.oscim.database.oscimap.Data)

# @@protoc_insertion_point(module_scope)
