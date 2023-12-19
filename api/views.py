from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from djangoapp.models import Category,Post
from api.serializers import CategorySerializer,PostSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer