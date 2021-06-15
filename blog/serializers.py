from blog.models import User, Post, Comment
from rest_framework.serializers import ModelSerializer

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class PostSerializer(ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = "__all__"

class UserSerializer(ModelSerializer):
    blog_posts = PostSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = "__all__"