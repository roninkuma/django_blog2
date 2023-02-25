from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    content = models.TextField(default='Здесь будет описание', verbose_name='Описание')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='Изображение')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def get_photo(self):
        if self.photo:
            url = self.photo.url
        else:
            url = 'https://i.ytimg.com/vi/3sTCJfIaFLM/maxresdefault.jpg'
        return url

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
