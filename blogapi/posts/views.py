from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Posts

# Create your views here.

class PostList(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


