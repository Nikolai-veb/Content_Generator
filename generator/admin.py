from django.contrib import admin
from .models import Categories, Under_Categories, Sites, Articles

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = { 'slug': ('name',) }


@admin.register(Under_Categories)
class Under_CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = { 'slug': ('name',) }


@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'url')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = { 'slug': ('name',) }


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'url')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = { 'slug': ('name',) }
