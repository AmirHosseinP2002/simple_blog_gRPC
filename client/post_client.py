import grpc

from django.contrib.auth.models import User

from protos.blog_proto import post_pb2, post_pb2_grpc
from blog.models import Category
from utils.image_process import read_image_as_base64


user = User.objects.get(id=1)
category = Category.objects.get(id=1)


image_data = read_image_as_base64('image.jpg')


with grpc.insecure_channel('localhost:50051') as channel:
    stub = post_pb2_grpc.PostControllerStub(channel)
    print('----- Create -----')
    response = stub.Create(post_pb2.Post(
            title='t1',  
            content='c1', 
            author=user.id, 
            category=category.id,
            image=image_data
        )
    )
    print(response, end='')
    print('----- List -----')
    for post in stub.List(post_pb2.PostListRequest()):
        print(post, end='')
    print('----- Retrieve -----')
    response = stub.Retrieve(post_pb2.PostRetrieveRequest(id=response.id))
    print(response, end='')
    print('----- Update -----')
    response = stub.Update(post_pb2.Post(
            id=response.id, 
            title='t2', 
            content='c2', 
            author=user.id,
            category=category.id, 
            image=image_data
        )
    )
    print(response, end='')
    print('----- Delete -----')
    stub.Destroy(post_pb2.Post(id=response.id))
