from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic.edit import FormMixin

from .models import Poet, Book, Section, Comment, Favorite
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        sections = book.sections.all()
        context["sections"] = sections

        return context
    

class SectionListView(generic.ListView):
    queryset = Section.objects.filter(active=True)
    template_name = 'qandeel/section_list.html'
    context_object_name = 'sections'
    ordering = 'title'


class SectionDetailView(FormMixin, generic.DetailView):
    model = Section
    template_name = 'qandeel/section_detail.html'
    context_object_name = 'section'
    form_class = CommentForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section = self.get_object()
        form = self.get_form()
        comments = Comment.active_comments_manager.filter(section=section)

        is_in_favorites = False
        if self.request.user.is_authenticated:
            is_in_favorites = Favorite.objects.filter(user=self.request.user, section=section).exists()
        
        context["form"] = form
        context["comments"] = comments
        context["is_in_favorites"] = is_in_favorites
        
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
    
    def get_success_url(self):
        return reverse('qandeel:section_detail', kwargs={'slug': self.object.slug})


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
    

class AddToFavoritesView(generic.CreateView):
    model = Favorite
    template_name = 'qandeel/section_detail.html'

    def form_valid(self, form):
        section_slug = form.cleaned_data['section_slug']
        section = get_object_or_404(Section, slug=section_slug)
        Favorite.objects.get_or_create(user=self.request.user, section=section)
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('qandeel:section_detail', kwargs={'slug': self.kwargs['section_slug']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['section_slug'] = self.kwargs['section_slug']

        return kwargs
    
    def post(self, request, *args, **kwargs):
        section_slug = kwargs['section_slug']
        section = get_object_or_404(Section, slug=section_slug)

        if not Favorite.objects.filter(user=request.user, section=section).exists():
            favorite = Favorite(user=request.user, section=section)
            favorite.save()
            
        return redirect('qandeel:section_detail', slug=section_slug)