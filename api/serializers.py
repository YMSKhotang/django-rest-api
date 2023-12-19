from rest_framework import serializers
from djangoapp.models import Category, Post

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields="__all__"

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields="__all__"
        #fields =['title','body']

