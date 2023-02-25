from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'photo', 'views', 'created_at', 'update_at', 'category']
    list_display_links = ['id', 'title']
    list_editable = ['content','photo']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
