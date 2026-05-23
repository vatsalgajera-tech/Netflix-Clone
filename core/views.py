from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Content, Category, Banner, MyList

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider_items'] = list(Content.objects.filter(is_active=True, poster_url__isnull=False).exclude(poster_url='')[:4])
        context['trending'] = Content.objects.filter(is_active=True)[:12]
        context['movies'] = Content.objects.filter(content_type='Movie', is_active=True)[:12]
        context['series'] = Content.objects.filter(content_type='Series', is_active=True)[:12]
        context['categories'] = Category.objects.filter(is_active=True).prefetch_related('content_set')
        return context

class MoviesView(TemplateView):
    template_name = 'core/movies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Content.objects.filter(content_type='Movie', is_active=True)
        context['categories'] = Category.objects.filter(is_active=True)
        context['selected_category'] = self.request.GET.get('category', '')
        if context['selected_category']:
            context['movies'] = context['movies'].filter(category__name=context['selected_category'])
        return context

class SeriesView(TemplateView):
    template_name = 'core/series.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['series'] = Content.objects.filter(content_type='Series', is_active=True)
        context['categories'] = Category.objects.filter(is_active=True)
        context['selected_category'] = self.request.GET.get('category', '')
        if context['selected_category']:
            context['series'] = context['series'].filter(category__name=context['selected_category'])
        return context

class ContentDetailView(DetailView):
    model = Content
    template_name = 'core/detail.html'
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = self.get_object()
        context['related'] = Content.objects.filter(
            category=content.category, is_active=True
        ).exclude(pk=content.pk)[:6]
        context['reviews'] = content.review_set.all()[:5]
        
        if self.request.user.is_authenticated:
            context['in_list'] = MyList.objects.filter(user=self.request.user, content=content).exists()
        else:
            context['in_list'] = False
            
        return context

class WatchView(LoginRequiredMixin, DetailView):
    model = Content
    template_name = 'core/watch.html'
    context_object_name = 'content'

class SearchView(TemplateView):
    template_name = 'core/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            context['results'] = Content.objects.filter(title__icontains=query, is_active=True)
        else:
            context['results'] = []
        context['query'] = query
        return context

class MyListToggleView(LoginRequiredMixin, View):
    def get(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        my_list_item = MyList.objects.filter(user=request.user, content=content)
        if my_list_item.exists():
            my_list_item.delete()
        else:
            MyList.objects.create(user=request.user, content=content)
        return redirect('core:detail', pk=pk)

class MyListView(LoginRequiredMixin, TemplateView):
    template_name = 'core/my_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_list = MyList.objects.filter(user=self.request.user).select_related('content').order_by('-added_at')
        context['my_list'] = [item.content for item in user_list if item.content.is_active]
        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'
