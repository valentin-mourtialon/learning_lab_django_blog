from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    # The second argument is a string representing the subdirectory inside the
    # templates directory in which our html file lives.
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    # By default, the list view wants to loop over the variable "object_list"
    # But we can change that behavior with:
    context_object_name = "posts"
    ordering = ["-date_posted"]  # The minus sign = Newest (top) to Oldest (bottom)
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(
            User, username=self.kwargs.get("username")
        )  # username in the URL parameter
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    # Template = /blog/post_detail.html
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # Beware "_form" !
    # Template = /blog/post_form.html
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user  # The current logged in user
        return super().form_valid(form)


# The inheritance order is important !
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Beware "_form" !
    # Template = /blog/post_form.html
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user  # The current logged in user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # type: ignore
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Template = /blog/post_detail.html
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # type: ignore
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
