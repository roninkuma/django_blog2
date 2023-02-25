from django.shortcuts import render
from .models import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    context = {
        'title': 'Главная страница',
        'categories': categories,
        'articles': articles
    }
    return render(request, 'blog/index.html', context)


# Выводит статьи определенной категории
def category_view(request, pk):
    # Вытащили все категории
    categories = Category.objects.all()
    # Вытащили категорию по pk
    category = Category.objects.get(pk=pk)
    # Вытащили все статьи из этой категории которую ранее определили
    articles = Article.objects.filter(category=category)
    # Создадим специфический путь
    context = {
        'categories': categories,
        'title': f'Категория: {category.title}',
        'articles': articles
    }
    return render(request, 'blog/index.html', context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'title': f'Статья: {article.title}',
        'article': article
    }
    return render(request, 'blog/article_detail.html', context)
