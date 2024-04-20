import grpc

from django.contrib.auth.models import User
from django_grpc_framework.test import RPCTestCase, Channel

from protos.blog_proto import post_pb2, post_pb2_grpc, category_pb2, category_pb2_grpc, comment_pb2, comment_pb2_grpc
from .models import Post, Category, Comment
from utils.image_process import read_image_as_base64


class PostServiceTest(RPCTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.channel = Channel()
        cls.stub = post_pb2_grpc.PostControllerStub(cls.channel)
        cls.user = User.objects.create(username='test_user')
        cls.image_data = read_image_as_base64('image.jpg')
        cls.category = Category.objects.create(
            title='cat1', description='description1'
        )
        cls.post_1 = Post.objects.create(
            title='title1', content='content1', author=cls.user, category=cls.category, image=cls.image_data
        )
        cls.post_2 = Post.objects.create(
            title='title2', content='content2', author=cls.user, category=cls.category, image=cls.image_data
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
            title='title', 
            content='content', 
            author=self.user.id,
            category=self.category.id,
            image=self.image_data
        ))
        self.assertEqual(response.title, 'title')
        self.assertEqual(response.content, 'content')

    def test_update_post(self):
        response = self.stub.Update(post_pb2.Post(
            id=self.post_1.id,
            title='title update',
            content='content update',
            author=self.user.id,
            category=self.category.id,
            image=self.image_data
        ))
        self.assertEqual(response.title, 'title update')
        self.assertEqual(response.content, 'content update')

    def test_delete_post(self):
        self.stub.Destroy(post_pb2.Post(id=self.post_1.id))
        self.assertEqual(Post.objects.count(), 1)


class CategoryServiceTest(RPCTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.channel = Channel()
        cls.stub = category_pb2_grpc.CategoryControllerStub(cls.channel)
        cls.category_1 = Category.objects.create(
            title='cat1', description='description1'
        )
        cls.category_2 = Category.objects.create(
            title='cat2', description='description2'
        )

    def test_detail_category(self):
        response = self.stub.Retrieve(
            category_pb2.CategoryRetrieveRequest(id=self.category_1.pk)
        )
        self.assertEqual(response.id, 1)

    def test_status_404_detail_category(self):
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.Retrieve(category_pb2.CategoryRetrieveRequest(id=999999))

        self.assertEqual(context.exception.code(), grpc.StatusCode.NOT_FOUND)

    def test_list_category(self):
        category_list = list(self.stub.List(category_pb2.CategoryListRequest()))
        self.assertEqual(len(category_list), 2)

    def test_create_category(self):
        response = self.stub.Create(category_pb2.Category(
            title='title_test', 
            description='description_test', 
        ))
        self.assertEqual(response.title, 'title_test')
        self.assertEqual(response.description, 'description_test')

    def test_update_category(self):
        response = self.stub.Update(category_pb2.Category(
            id=self.category_1.id,
            title='title update',
            description='description update',
        ))
        self.assertEqual(response.title, 'title update')
        self.assertEqual(response.description, 'description update')

    def test_delete_category(self):
        self.stub.Destroy(category_pb2.Category(id=self.category_1.id))
        print(Category.objects.all())
        self.assertEqual(Category.objects.count(), 1)


class CommentServiceTest(RPCTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.channel = Channel()
        cls.stub = comment_pb2_grpc.CommentControllerStub(cls.channel)
        cls.category = Category.objects.create(
            title='cat1', description='description1'
        )
        cls.user = User.objects.create(username='test_user')
        cls.image_data = read_image_as_base64('image.jpg')
        cls.post_1 = Post.objects.create(
            title='title1', content='content1', author=cls.user, category=cls.category, image=cls.image_data
        )
        cls.comment_1 = Comment.objects.create(
            author=cls.user, post=cls.post_1, body='body 1'
        )
        cls.comment_2 = Comment.objects.create(
            author=cls.user, post=cls.post_1, body='body 2'
        )

    def test_detail_comment(self):
        response = self.stub.Retrieve(
            comment_pb2.CommentRetrieveRequest(id=self.comment_1.pk)
        )
        self.assertEqual(response.id, 1)

    def test_status_404_detail_comment(self):
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.Retrieve(comment_pb2.CommentRetrieveRequest(id=999999))

        self.assertEqual(context.exception.code(), grpc.StatusCode.NOT_FOUND)

    def test_list_comment(self):
        comment_list = list(self.stub.List(comment_pb2.CommentListRequest()))
        self.assertEqual(len(comment_list), 2)

    def test_create_comment(self):
        response = self.stub.Create(comment_pb2.Comment(
            body='body test', 
            author=self.user.id,
            post=self.post_1.id 
        ))
        self.assertEqual(response.body, 'body test')
        self.assertEqual(response.post, self.post_1.id)

    def test_update_comment(self):
        response = self.stub.Update(comment_pb2.Comment(
            id=self.comment_1.id,
            body='body update',
            author=self.user.id,
            post=self.post_1.id 
        ))
        self.assertEqual(response.body, 'body update')
        self.assertEqual(response.author, self.user.id)

    def test_delete_comment(self):
        self.stub.Destroy(comment_pb2.Comment(id=self.comment_1.id))
        self.assertEqual(Comment.objects.count(), 1)

