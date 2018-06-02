from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<category>/<slug>/', views.post_detail, name='post_detail'),
    path('category/posts/<name>/', views.cat_detail, name='cat_detail'),
]
