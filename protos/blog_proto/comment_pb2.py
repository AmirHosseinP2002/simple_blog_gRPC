# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comment.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcomment.proto\x12\x07\x63omment\x1a\x1bgoogle/protobuf/empty.proto\"c\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x0f\n\x07\x63reated\x18\x03 \x01(\t\x12\x0f\n\x07updated\x18\x04 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\x05\x12\x0c\n\x04post\x18\x06 \x01(\x05\"\x14\n\x12\x43ommentListRequest\"$\n\x16\x43ommentRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xa6\x02\n\x11\x43ommentController\x12\x39\n\x04List\x12\x1b.comment.CommentListRequest\x1a\x10.comment.Comment\"\x00\x30\x01\x12.\n\x06\x43reate\x12\x10.comment.Comment\x1a\x10.comment.Comment\"\x00\x12?\n\x08Retrieve\x12\x1f.comment.CommentRetrieveRequest\x1a\x10.comment.Comment\"\x00\x12.\n\x06Update\x12\x10.comment.Comment\x1a\x10.comment.Comment\"\x00\x12\x35\n\x07\x44\x65stroy\x12\x10.comment.Comment\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'comment_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COMMENT']._serialized_start=55
  _globals['_COMMENT']._serialized_end=154
  _globals['_COMMENTLISTREQUEST']._serialized_start=156
  _globals['_COMMENTLISTREQUEST']._serialized_end=176
  _globals['_COMMENTRETRIEVEREQUEST']._serialized_start=178
  _globals['_COMMENTRETRIEVEREQUEST']._serialized_end=214
  _globals['_COMMENTCONTROLLER']._serialized_start=217
  _globals['_COMMENTCONTROLLER']._serialized_end=511
# @@protoc_insertion_point(module_scope)