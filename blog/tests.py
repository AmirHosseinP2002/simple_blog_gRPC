import grpc

from django.contrib.auth.models import User

from django_grpc_framework.test import RPCTestCase, Channel

from protos.blog_proto import post_pb2, post_pb2_grpc
from .models import Post


class PostServiceTest(RPCTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.channel = Channel()
        cls.stub = post_pb2_grpc.PostControllerStub(cls.channel)
        cls.user = User.objects.create(username='test_user')
        cls.post_1 = Post.objects.create(
            title='title1', content='content1', author=cls.user
        )
        cls.post_2 = Post.objects.create(
            title='title2', content='content2', author=cls.user
        )

    def test_detail_post(self):
        response = self.stub.Retrieve(
            post_pb2.PostRetrieveRequest(id=self.post_1.pk)
        )
        self.assertEqual(response.id, 1)

    def test_status_404_detail_post(self):
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.Retrieve(post_pb2.PostRetrieveRequest(id=999999))

        self.assertEqual(context.exception.code(), grpc.StatusCode.NOT_FOUND)

    def test_list_posts(self):
        post_list = list(self.stub.List(post_pb2.PostListRequest()))
        self.assertEqual(len(post_list), 2)

    def test_create_post(self):
        response = self.stub.Create(post_pb2.Post(
            title='title', content='content', author=self.user.id))
        self.assertEqual(response.title, 'title')
        self.assertEqual(response.content, 'content')

    def test_update_post(self):
        response = self.stub.Update(post_pb2.Post(
            id=self.post_1.id,
            title='title update',
            content='content update',
            is_active=False,
            author=self.user.id
        ))
        self.assertEqual(response.title, 'title update')
        self.assertEqual(response.content, 'content update')
        self.assertEqual(response.is_active, False)

    def test_delete_post(self):
        self.stub.Destroy(post_pb2.Post(id=self.post_1.id))
        self.assertEqual(Post.objects.count(), 1)
