from django.contrib import admin

from .models import Century, Poet, Book, Poem, Section

@admin.register(Century)
class CenturyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

@admin.register(Poet)
class PoetAdmin(admin.ModelAdmin):
    list_display = ['name', 'century', 'created_at']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'poet', 'created_at']

@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'book', 'poem', 'created_at', 'modified_at']
