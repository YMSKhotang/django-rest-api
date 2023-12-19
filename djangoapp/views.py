from django.shortcuts import render

# Create your views here.
from djangoapp.models import Post


def demo(request):
    return render(request,"djangoapp/demo.html")



def blogs(request):
    posts = Post.objects.all().order_by("-created_on")
    context={
        "posts" : posts,
    }
    return render(request,"djangoapp/index.html",context)
    