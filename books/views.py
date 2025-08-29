from django.shortcuts import render,get_object_or_404,redirect
from .models import Book,Book_on_sale,BorrowHistory
from django.urls import reverse_lazy
from django.views import View
from django.utils import timezone
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context={
        'books': Book.objects.all()
    }
    return render(request, 'books/home.html',context)

def about(request):
    return render(request, 'books/about.html', {'title':'About'})

class Book_on_saleListView(ListView):
    model = Book_on_sale
    template_name = "books/home.html"
    context_object_name = "books_on_sale"

class BookListView(ListView):
    model = Book
    template_name='books/book_list.html' #<app>.<model>_<viewtype>.html
    context_object_name= 'books'
    ordering=['title','author']

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    fields=['title','author','genre','status']
    success_url = reverse_lazy('Your_Library')

    def get_initial(self):
        initial = super().get_initial()
        initial['title'] = self.request.GET.get('title', '')
        initial['author'] = self.request.GET.get('author', '')
        initial['price'] = self.request.GET.get('price', '')
        return initial

class BookUpdateView(UpdateView):
    model = Book
    fields=['title','author','genre','status']
    success_url = reverse_lazy('Your_Library')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('Your_Library')

class BorrowHistoryListView(ListView):
    model = BorrowHistory
    template_name = 'books/borrow_history.html'
    context_object_name = 'histories'
    ordering = ['-borrowed_at']

class BorrowBookView(View):

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.status="reading"
        book.save()
        BorrowHistory.objects.create(book=book)
        return redirect('Your_Library')

class ReturnBookView(View):

    def post(self,request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.status = "completed"
        book.save()
        histories=BorrowHistory.objects.filter(book_id=book.id)

        history = BorrowHistory.objects.filter(book=book, returned_at__isnull=True).last()
        if history:
            history.returned_at = timezone.now()
            history.save()

        return redirect('Your_Library')
