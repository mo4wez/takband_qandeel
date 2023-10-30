from django.db import models


class Century(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Poet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    century = models.ForeignKey(to=Century, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    poet = models.ForeignKey(to=Poet, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Poem(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Section(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    poem = models.OneToOneField(to=Poem, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)