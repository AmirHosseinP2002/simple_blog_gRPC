import grpc

from django.contrib.auth.models import User

from protos.blog_proto import comment_pb2, comment_pb2_grpc
from blog.models import Post


user = User.objects.get(id=1)
post = Post.objects.get(id=1)


with grpc.insecure_channel('localhost:50051') as channel:
    stub = comment_pb2_grpc.CommentControllerStub(channel)
    print('----- Create -----')
    response = stub.Create(comment_pb2.Comment(
            body='b1', 
            post=post.id,
            author=user.id
        )
    )
    print(response, end='')
    print('----- List -----')
    for comment in stub.List(comment_pb2.CommentListRequest()):
        print(comment, end='')
    print('----- Retrieve -----')
    response = stub.Retrieve(comment_pb2.CommentRetrieveRequest(id=response.id))
    print(response, end='')
    print('----- Update -----')
    response = stub.Update(comment_pb2.Comment(
            id=response.id, 
            body='b2', 
            post=post.id,
            author=user.id
        )
    )
    print(response, end='')
    print('----- Delete -----')
    stub.Destroy(comment_pb2.Comment(id=response.id))