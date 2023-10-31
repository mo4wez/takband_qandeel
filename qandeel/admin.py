from django.contrib import admin

from .models import Century, Poet, Book, PoeticFormat, Section, Comment


@admin.register(Century)
class CenturyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at',] 

@admin.register(Poet)
class PoetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'century', 'created_at',]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'poet', 'created_at',]

@admin.register(PoeticFormat)
class PoeticFormatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at',]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'book', 'poetic_format', 'created_at', 'modified_at',]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'section', 'status', 'active',]
