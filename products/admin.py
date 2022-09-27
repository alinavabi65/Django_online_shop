from django.contrib import admin

from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]

    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['products', 'author', 'stars', 'datetime_create', 'datetime_modified', 'active', ]

