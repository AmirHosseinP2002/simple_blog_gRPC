from django_grpc_framework import proto_serializers

from .models import Category, Post, Comment
from protos.blog_proto import post_pb2, category_pb2, comment_pb2


class PostProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Post
        proto_class = post_pb2.Post
        fields = ['id', 'title', 'content', 'category', 'image',
                  'is_active', 'author', 'created', 'updated']


class CategoryProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Category
        proto_class = category_pb2.Category
        fields = ['id', 'title', 'description']


class CommentProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Comment
        proto_class = comment_pb2.Comment
        fields = ['id', 'author', 'post', 'body', 'created', 'updated']
