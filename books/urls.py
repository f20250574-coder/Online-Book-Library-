from django.urls import path
from . import views
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    Book_on_saleListView,
    BookDeleteView,
    BorrowHistoryListView,
    BorrowBookView,
    ReturnBookView
)

urlpatterns = [
    path('', Book_on_saleListView.as_view(), name='Library-home'),
    path('Your_Library/', BookListView.as_view(), name='Your_Library'),
    path('about/', views.about, name='Library-about'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/detail/', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/',BookDeleteView.as_view(),name='book-delete'),
    path('borrow-history/', BorrowHistoryListView.as_view(), name='borrow-history'),
    path('book/<int:pk>/borrow/', BorrowBookView.as_view() ,name='book-borrow'),
    path('book/<int:pk>/return/', ReturnBookView.as_view() ,name='book-return')
] 
