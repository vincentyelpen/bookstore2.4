from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Book ID: {self.id} Title: {self.title}"
