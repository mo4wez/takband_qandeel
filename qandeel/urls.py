from django.urls import path

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
    path('poets/<int:pk>/', PoetDetailView.as_view(), name='poet_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('poets/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('sections/', SectionListView.as_view(), name='section_list'),
    path('sections/<int:pk>/', SectionDetailView.as_view(), name='section_detail')
]
