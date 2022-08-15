from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Posts
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostList(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


