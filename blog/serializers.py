from blog.models import User, Post, Comment
from rest_framework.serializers import ModelSerializer

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'post', 'body', 'created', 'updated')

class PostSerializer(ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('title', 'user', 'body', 'publish', 'created', 'updated', 'comments')

class UserSerializer(ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('name', 'lastname', 'age', 'posts')