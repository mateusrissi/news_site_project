from django.contrib import admin
from .models import Post, Author, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_on', 'published']
    list_filter = ("published", "category","author",)
    search_fields = ['title', 'author__name', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
