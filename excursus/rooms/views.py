from django.shortcuts import render, get_object_or_404
from .models import Category,Post
from django.views import generic
from django.db.models import Max
from django.contrib.auth.decorators import login_required
# Create your views here.

def category(request, slug):
    cat = get_object_or_404(Category, slug=slug)

    return render(request, "category.html", {
        "category": cat,
        "posts": cat.posts.order_by("-created_date"),
    })

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, "post.html", {
        "post": post,
        "posts": post.comments.order_by("created_date"),
    })

@login_required
def index(request):

    category = Category.objects.annotate(
        max_created=Max("created_date")
    ).order_by("-max_created")

    # Render that in the index template
    return render(request, "index.html", {
        "category": category,
    })

class PostDetailView(generic.DetailView):
    model=Post
