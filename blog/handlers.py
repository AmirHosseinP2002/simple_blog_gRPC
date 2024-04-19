from .services import PostService, CategoryService, CommentService
from protos.blog_proto import post_pb2_grpc, category_pb2_grpc, comment_pb2_grpc


def grpc_handlers(server):
    post_pb2_grpc.add_PostControllerServicer_to_server(
        PostService.as_servicer(),
        server
    )
    category_pb2_grpc.add_CategoryControllerServicer_to_server(
        CategoryService.as_servicer(),
        server
    )
    comment_pb2_grpc.add_CommentControllerServicer_to_server(
        CommentService.as_servicer(),
        server
    )
