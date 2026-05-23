from django.contrib import admin
from .models import Category, Genre, Content, Banner, WatchHistory, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_type', 'release_year', 'category', 'is_active']
    list_filter = ['content_type', 'is_active', 'category']
    search_fields = ['title']
    filter_horizontal = ['genres']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'rating']

@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'watched_at']
