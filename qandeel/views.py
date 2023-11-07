from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin

from .models import Poet, Book, Section, Comment
from .forms import CommentForm


class PoetListView(generic.ListView):
    queryset = Poet.objects.all()
    template_name = 'qandeel/poet_list.html'
    context_object_name = 'poets'
    ordering = 'name'


class PoetDetailView(generic.DetailView):
    model = Poet
    template_name = 'qandeel/poet_detail.html'
    context_object_name = 'poet'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poet = self.get_object()
        books = poet.books.all()
        context["books"] = books

        return context
    

class BookListView(generic.ListView):
    queryset = Book.objects.all()
    template_name = 'qandeel/book_list.html'
    context_object_name = 'books'
    ordering = 'name'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'qandeel/book_detail.html'
    context_object_name = 'book'


class SectionListView(generic.ListView):
    queryset = Section.objects.all()
    template_name = 'qandeel/section_list.html'
    context_object_name = 'sections'
    ordering = 'title'


class SectionDetailView(FormMixin, generic.DetailView):
    model = Section
    template_name = 'qandeel/section_detail.html'
    context_object_name = 'section'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('qandeel:section_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section = self.get_object()
        form = self.get_form()
        comments = section.comments.all()
        context["form"] = form
        context["comments"] = comments
        
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.section = self.object
        obj.save()

        return super().form_valid(form)
    

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        section_slug = self.kwargs['slug']
        section = get_object_or_404(Section, slug=section_slug)
        obj.section = section

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('qandeel:section_detail', kwargs={'slug': self.kwargs['slug']})
    
