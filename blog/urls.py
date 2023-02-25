from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:pk>', category_view, name='category'),
    path('article/<int:pk>', article_detail, name='article'),
    path('add_article', add_article, name='add_article')
]
