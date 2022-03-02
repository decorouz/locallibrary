from django.shortcuts import render
from django.views import generic
from .models import Author, Book, BookInstance, Genre

# Create your views here.
def index(request):
    """View function for home page of site"""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = "a")
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    num_authors = Author.objects.count()
    num_sci_genre = Book.objects.filter(genre__name__icontains="science").count()
    num_of_book_contain_war = Book.objects.filter(title__icontains="war").count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_sci_genre": num_sci_genre,
        "num_sci_genre": num_sci_genre,
        "num_of_book_contain_war": num_of_book_contain_war,
    }

    return render(request, "index.html", context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
