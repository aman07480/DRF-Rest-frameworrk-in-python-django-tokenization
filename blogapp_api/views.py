from django.shortcuts import render
from rest_framework import generics
from blogapp_api.serializers import PostSerializer
from blogapp.models import Post
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions,SAFE_METHODS,BasePermission
# Create your views here.


# class PostUserWritePernission(BasePermission):
#     message='Editing Posts is restricted  to the author only'
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.author == request.user
        

class PostList(generics.ListCreateAPIView):
    permission_classes=[DjangoModelPermissions]
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    

""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""