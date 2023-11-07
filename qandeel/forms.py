from django import forms
from django.forms import ModelForm

from .models import Comment, Favorite

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }


class AddToFavoritesForm(forms.Form):
    section_slug = forms.CharField(widget=forms.HiddenInput())


class FavoriteForm(ModelForm):
    class Meta:
        model = Favorite
        fields = []

    def __init__(self, *args, **kwargs):
        section_slug = kwargs.pop('section_slug', None)
        super(FavoriteForm, self).__init__(*args, **kwargs)
        if section_slug:
            self.fields['section_slug'] = forms.CharField(widget=forms.HiddenInput(), initial=section_slug)
