from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Poet, Book, Section, Comment
from .forms import CommentForm


class PoetListView(generic.ListView):
    queryset = Poet.objects.all()
    paginate_by = 4
    template_name = 'qandeel/poet_list.html'
    context_object_name = 'poets'


class PoetDetailView(generic.DetailView):
    model = Poet
    template_name = 'qandeel/poet_detail.html'
    context_object_name = 'poet'


class BookListView(generic.ListView):
    queryset = Book.objects.all()
    paginate_by = 6
    template_name = 'qandeel/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'qandeel/book_detail.html'
    context_object_name = 'book'


class SectionListView(generic.ListView):
    queryset = Section.objects.all()
    paginate_by = 10
    template_name = 'qandeel/section_list.html'
    context_object_name = 'sections'


class SectionDetailView(generic.DetailView):
    model = Section
    template_name = 'qandeel/section_detail.html'
    context_object_name = 'section'

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user

        section_id = int(self.kwargs('section_id'))
        section = get_object_or_404(Poet, id=section_id)
        obj.poet = section

        return super().form_valid(form)
    
