from django.urls import path
from . import views
urlpatterns = [
    path('', views.list, name = 'blog_home'),
    path('<int:id>/', views.article, name = 'article_id')
]
