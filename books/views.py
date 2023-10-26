from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView
from .models import Book
from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"

class BookCreateView(CreateView):
    model = Book
    template_name = "book_create.html"
    fields = ["title", "author", "description", "published_date", "price"]
    success_url = reverse_lazy("book_list")

class BookUpdateView(UpdateView):
    model = Book
    template_name = "book_edit.html"
    fields = ["title", "author", "description", "published_date", "price"]
    success_url = reverse_lazy("book_list")

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("book_list")