from django.urls import path, re_path

from .views import (
    PoetListView,
    PoetDetailView,
    BookListView,
    BookDetailView,
    SectionListView,
    SectionDetailView,
    CommentCreateView,
    )

app_name = 'qandeel'

urlpatterns = [
    path('poets/', PoetListView.as_view(), name='poet_list'),
    re_path('poets/(?P<slug>[-\w]+)/', PoetDetailView.as_view(), name='poet_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
    re_path('books/(?P<slug>[-\w]+)/', BookDetailView.as_view(), name='book_detail'),
    path('sections/', SectionListView.as_view(), name='section_list'),
    re_path('sections/(?P<slug>[-\w]+)/', SectionDetailView.as_view(), name='section_detail'),
    path(r'^comment/(?P<slug>[-\w]+)/', CommentCreateView.as_view(), name='comment_create'),
]
