from django.shortcuts import render
from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    # The second argument is a string representing the subdirectory inside the
    # templates directory in which our html file lives.
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
