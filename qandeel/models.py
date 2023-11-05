from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from slugify import slugify
from django_extensions.db.fields import AutoSlugField


def custom_slugify(value):
    """
    Convert non-English characters to ASCII characters and then create a slug.

    """

    return slugify(value, separator='-', allow_unicode=True)



class Century(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Centuries'

    def __str__(self):
        return self.name


class Poet(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['name'], unique=True, allow_unicode=True, slugify_function=custom_slugify)
    description = models.TextField()
    century = models.ForeignKey(to=Century, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)
        super(Poet, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("qandeel:poet_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['name'], unique=True, allow_unicode=True, slugify_function=custom_slugify)
    description = models.TextField()
    poet = models.ForeignKey(to=Poet, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("qandeel:book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class PoeticFormat(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['title'], unique=True, allow_unicode=True, slugify_function=custom_slugify)
    body = models.TextField()
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    poetic_format = models.ForeignKey(to=PoeticFormat, related_name='sections', on_delete=models.CASCADE)
    topic = models.ForeignKey(to=Topic, related_name='sections', null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)
        super(Section, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("qandeel:section_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    COMMENT_WAITING = 'wa'
    COMMENT_APPROVED = 'ap'
    COMMENT_NOT_APPROVED = 'na'

    STATUS_CHOICES = [
        (COMMENT_WAITING,'Waiting'),
        (COMMENT_APPROVED,'Approved'),
        (COMMENT_NOT_APPROVED,'Not Approved'),
    ]

    section = models.ForeignKey(to=Section, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='Leave a comment')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=COMMENT_WAITING)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'comment {self.id}'


