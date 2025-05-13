from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_bookmarks, name='list_bookmarks'),
    path('add/', views.add_bookmark, name='add_bookmark'),
    path('edit/<int:bookmark_id>/', views.edit_bookmark, name='edit_bookmark'),
    path('delete/<int:bookmark_id>/', views.delete_bookmark, name='delete_bookmark'),
    path('search/', views.search_bookmarks, name='search_bookmarks'),
]