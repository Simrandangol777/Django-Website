from django.contrib import admin
from . models import Category, Blog
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email')

class BlogAdmin(admin.ModelAdmin):
    exclude=('created_at',)
    list_display=('id', 'title', 'content')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
