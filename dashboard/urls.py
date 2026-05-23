from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name='home'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('movies/', views.MovieListView.as_view(), name='movies'),
    path('series/', views.SeriesListView.as_view(), name='series'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
]
