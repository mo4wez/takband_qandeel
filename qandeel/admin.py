from django.contrib import admin
from django.http.request import HttpRequest
from django.db.models import Count

from .models import Century, Poet, Book, PoeticFormat, Section, Comment


@admin.register(Century)
class CenturyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at',] 

@admin.register(Poet)
class PoetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'century', 'created_at',]
    list_per_page = 10
    search_fields = ['name',]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'poet', 'created_at',]
    list_per_page = 10
    search_fields = ['name', 'book',]

@admin.register(PoeticFormat)
class PoeticFormatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at',]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'book', 'poetic_format', 'num_of_comments', 'modified_at',]
    list_per_page = 20

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request) \
            .prefetch_related('comments') \
            .annotate(comments_count=Count('comments'))

    @admin.display(ordering='comments_count', description='# comments')
    def num_of_comments(self, section: Section):
        return section.comments_count

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'section', 'status', 'active',]
    list_editable = ['status', 'active',]
    list_per_page = 20
