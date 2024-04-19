import base64
import grpc

from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from django_grpc_framework import mixins
from django_grpc_framework import generics
from django.core.files.base import ContentFile

from .models import Category, Post, Comment
from .serializers import CategoryProtoSerializer, CommentProtoSerializer, PostProtoSerializer


# Generate PostService with Service
# class PostService(Service):
#     def List(self, request, context):
#         posts = Post.objects.all()
#         serializer = PostProtoSerializer(posts, many=True)
#         for msg in serializer.message:
#             yield msg

#     def Create(self, request, context):
#         serializer = PostProtoSerializer(message=request)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return serializer.message

#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             self.context.abort(grpc.StatusCode.NOT_FOUND, f'Post: {pk} not found!')

#     def Retrieve(self, request, context):
#         post = self.get_object(request.id)
#         serializer = PostProtoSerializer(post)
#         return serializer.message

#     def Update(self, request, context):
#         post = self.get_object(request.id)
#         serializer = PostProtoSerializer(post, message=request)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return serializer.message

#     def Destroy(self, request, context):
#         post = self.get_object(request.id)
#         post.delete()
#         return empty_pb2.Empty()


# Generate PostService with GenericService and mixins
# class PostService(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   generics.GenericService):
#     queryset = Post.objects.all()
#     serializer_class = PostProtoSerializer


# Generate PostService with ModelService
class PostService(generics.ModelService):
    queryset = Post.objects.all()
    serializer_class = PostProtoSerializer

    def get_image_file_from_base64(self, image):
        image_data = base64.b64decode(self.request.image)
        image_file = ContentFile(image_data, name='image.jpg')
        return image_file

    def Create(self, request, context):
        image_file = self.get_image_file_from_base64(request.image)

        serializer = PostProtoSerializer(data={
            'title': request.title,
            'content': request.content,
            'image': image_file,
            'category': request.category,
            'author': request.author,
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Update(self, request, context):
        image_file = self.get_image_file_from_base64(request.image)

        serializer = PostProtoSerializer(data={
            'title': request.title,
            'content': request.content,
            'image': image_file,
            'category': request.category,
            'author': request.author,
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message


class CategoryService(generics.ModelService):
    queryset = Category.objects.all()
    serializer_class = CategoryProtoSerializer


class CommentService(generics.ModelService):
    queryset = Comment.objects.all()
    serializer_class = CommentProtoSerializer
