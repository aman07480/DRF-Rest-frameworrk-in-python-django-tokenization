from django.contrib import admin
from django.urls import path
from .views import PostList,PostDetail

app_name='blogapp_api'

urlpatterns = [
    path('<int:pk>/',PostDetail.as_view(),name='post-detail'),
    path('posts/',PostList.as_view(),name='post-list'),
]
