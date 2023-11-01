from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class Century(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Centuries'


    def __str__(self):
        return self.name

def my_slugify_function(content):
    return slugify(content, allow_unicode=True)


class Poet(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    century = models.ForeignKey(to=Century, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super(Poet, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True ,blank=True)
    description = models.TextField()
    poet = models.ForeignKey(to=Poet, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PoeticFormat(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True ,blank=True)
    body = models.TextField()
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    poetic_format = models.ForeignKey(to=PoeticFormat, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

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

