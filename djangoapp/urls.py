from django.urls import path
from djangoapp import views

urlpatterns = [
    path("demo/", views.demo),
    path('',views.blogs, name='blogs')
]

