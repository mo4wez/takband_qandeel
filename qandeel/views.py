from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Poet, Book, Section


class PoetListView(generic.ListView):
    queryset = Poet.objects.all()
    paginate_by = 4
    template_name = 'qandeel/poet_list.html'
    context_object_name = 'poets'


class PoetDetailView(generic.DetailView):
    model = Poet
    template_name = 'qandeel/poet_detail.html'
    context_object_name = 'poet'
