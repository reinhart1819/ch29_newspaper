from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

# Create your views here.

class ArticleListView(ListView):
    template_name = 'articles/list.html'
    model = Article

class ArticleDetailView(DetailView):
    template_name = 'articles/detail.html'
    model = Article

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/delete.html'
    model = Article
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'articles/edit.html'
    model = Article
    fields = ['title', 'category', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(CreateView, LoginRequiredMixin):
    template_name = 'articles/new.html'
    model = Article
    fields = ['title', 'category', 'body', 'author']