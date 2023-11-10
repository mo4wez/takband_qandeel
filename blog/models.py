from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from qandeel.models import custom_slugify

class Post(models.Model):
    POST_PUBLISHED = 'pub'
    POST_DRAFT = 'drf'

    STATUS_CHOICES = (
        (POST_PUBLISHED, 'published'),
        (POST_DRAFT, 'draft'),
    )

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['title'], unique=True, allow_unicode=True, slugify_function=custom_slugify)
    content = RichTextField()
    author = models.ForeignKey(to=get_user_model(), related_name='posts', on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=POST_DRAFT)
    active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    

