from django.urls import path, re_path

from .views import (
    PoetListView,
    PoetDetailView,
    BookListView,
    BookDetailView,
    SectionListView,
    SectionDetailView
    )

app_name = 'qandeel'

urlpatterns = [
    path('poets/', PoetListView.as_view(), name='poet_list'),
    re_path('poets/(?P<slug>[-\w]+)/', PoetDetailView.as_view(), name='poet_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
    re_path('books/(?P<slug>[-\w]+)/', BookDetailView.as_view(), name='book_detail'),
    path('sections/', SectionListView.as_view(), name='section_list'),
    path('sections/<slug:slug>/', SectionDetailView.as_view(), name='section_detail')
]
