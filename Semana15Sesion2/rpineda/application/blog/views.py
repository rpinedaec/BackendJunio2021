from django.shortcuts import render
from django.views import generic
from .serializers import AuthorSerializer, TagSerializer, PostSerializer
from .models import Author,Tag,Post
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(author__username=username)
    #     return queryset
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'content']
    # search_fields = ('title', 'content')
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('title',)
