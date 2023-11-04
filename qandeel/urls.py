from django.urls import path

from .views import PoetListView, PoetDetailView

app_name = 'qandeel'

urlpatterns = [
    path('', PoetListView.as_view(), name='poet_list'),
    path('<int:pk>/', PoetDetailView.as_view(), name='poet_detail'),
]
