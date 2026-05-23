from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('movies/', views.MoviesView.as_view(), name='movies'),
    path('series/', views.SeriesView.as_view(), name='series'),
    path('detail/<int:pk>/', views.ContentDetailView.as_view(), name='detail'),
    path('watch/<int:pk>/', views.WatchView.as_view(), name='watch'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('my-list/', views.MyListView.as_view(), name='my_list'),
    path('my-list/toggle/<int:pk>/', views.MyListToggleView.as_view(), name='my_list_toggle'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
