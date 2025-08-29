from django.db import models as md
from django.urls import reverse

class Book(md.Model):
    STATUS_CHOICES = [
        ('reading', 'Reading'),
        ('completed', 'Completed'),
        ('wishlist', 'Wishlist'),
    ]

    title = md.CharField(max_length=200)
    author = md.CharField(max_length=100)
    genre = md.CharField(max_length=50)
    status = md.CharField(max_length=10, choices=STATUS_CHOICES, default='wishlist')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail',kwargs={'pk':self.pk})

class Book_on_sale(md.Model):
    title = md.CharField(max_length=200)
    author = md.CharField(max_length=100)
    genre = md.CharField(max_length=50)
    price = md.CharField(max_length=10)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail',kwargs={'pk':self.pk})


class BorrowHistory(md.Model):
    book = md.ForeignKey(Book, on_delete=md.CASCADE, related_name='history')
    borrowed_at = md.DateTimeField(auto_now_add=True)
    returned_at = md.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} borrowed on {self.borrowed_at}"
