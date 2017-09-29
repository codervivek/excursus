from django.shortcuts import render, get_object_or_404
from .models import Category,Post, Comment
from django.views import generic
from django.db.models import Max
from django.contrib.auth.decorators import login_required
# Create your views here.

# def category(request, slug):
#     cat = get_object_or_404(Category, slug=slug)

#     return render(request, "category.html", {
#         "category": cat,
#         "posts": cat.posts.order_by("-created_date"),
#     })

class CategoryListView(generic.ListView):
    model=Category
    paginate_by = 10

class CategoryDetailView(generic.DetailView):
    model=Category

class CommentDetailView(generic.DetailView):
    model=Comment
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        return redirect(self.object.post)

# def CategoryDetail(request, slug):
#     category = get_object_or_404(Category, slug=slug)
    # post = category.posts.annotate(
    #     max_created=Max("created_date")
    # ).order_by("-max_created")
    # post=category.posts.all
    # return render(request, "category_detail.html", {
    #     "category":category,
    #     "post": post,
    # })

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, "post.html", {
        "post": post,
        "posts": post.comments.order_by("created_date"),
    })

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    post = Post.objects.annotate(
        max_created=Max("created_date")
    ).order_by("-max_created")

    paginator = Paginator(post, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'post': posts, 'page_obj':posts, 'is_paginated':True})


    # Render that in the index template
    # return render(request, "index.html", {
    #     "post": post,
    # })

class PostDetailView(generic.DetailView):
    model=Post

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Category, Comment
from django.http import HttpResponseRedirect
class PostCreate(CreateView):
    model = Post
    fields = ['text','category','user','photo']
    labels = { 'text': ('Post text')}
    default_data={'user':'test'}

class PostUpdate(UpdateView):
    model = Post
    fields = ['text','category']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

class CategoryCreate(CreateView):
    model = Category
    fields = ['name','slug']

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('post')

class CommentCreate(CreateView):
    model = Comment
    fields = ['text','user','post']

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['text','user','post']

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('post')

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from excursus.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView

from rooms.models import Post


class SearchListView(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        qs = Post.objects.all()
        keywords = self.request.GET.get('q')
        if keywords:
            query = SearchQuery(keywords)
            vector = SearchVector('text','category__name')
            qs = qs.annotate(search=vector).filter(search=query)
            qs = qs.annotate(rank=SearchRank(vector, query)).order_by('-rank')

        return qs

# from django.forms import ModelForm
# class PostModelForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['text','category']

#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user')
#         super(PostModelForm, self).__init__(*args, **kwargs)

