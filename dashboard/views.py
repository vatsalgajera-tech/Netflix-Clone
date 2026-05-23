from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from users.models import CustomUser
from core.models import Content, Category, Genre, Banner

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/accounts/login/'
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

class DashboardHomeView(AdminRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users'] = CustomUser.objects.count()
        context['total_movies'] = Content.objects.filter(content_type='Movie').count()
        context['total_series'] = Content.objects.filter(content_type='Series').count()
        context['total_categories'] = Category.objects.count()
        context['recent_content'] = Content.objects.all().order_by('-created_at')[:10]
        return context

class UserListView(AdminRequiredMixin, ListView):
    model = CustomUser
    template_name = 'dashboard/users.html'
    context_object_name = 'users'

class MovieListView(AdminRequiredMixin, ListView):
    model = Content
    template_name = 'dashboard/movies.html'
    context_object_name = 'movies'
    def get_queryset(self):
        return Content.objects.filter(content_type='Movie').order_by('-created_at')

class SeriesListView(AdminRequiredMixin, ListView):
    model = Content
    template_name = 'dashboard/series.html'
    context_object_name = 'series'
    def get_queryset(self):
        return Content.objects.filter(content_type='Series').order_by('-created_at')

class CategoryListView(AdminRequiredMixin, ListView):
    model = Category
    template_name = 'dashboard/categories.html'
    context_object_name = 'categories'
