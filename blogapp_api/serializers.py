from rest_framework import serializers
from blogapp.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'exceprt', 'content', 'staus')
        model = Post
        # fields='__all__'
        # # fields=['title','author','slug