from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django.db.models import Q

from book.models import Book
from book.forms import SearchingBookForm, BookForm, IdForm
from order.models import Order
from author.models import Author

# Create your views here.

def index(request):
    return render(request, 'book/index.html')

def allbooks(request):
    book_objects = Book.objects.all()
    order_objects = Order.objects.all()
    searchForm = SearchingBookForm()
    id_form = IdForm()

    orders_book_id = []
    unordered_books_id = []
    for order in order_objects:
        orders_book_id.append(order.book.id)
    for book in book_objects:
        if book.id not in orders_book_id:
            unordered_books_id.append(book.id)

    context = {'book_objects': book_objects,
               'unordered_books_id': unordered_books_id,
               'form': searchForm,
               'id_form': id_form,
               }
    if searchForm.is_valid():
        context['book_objects'] = book_objects.filter(name__startswith=searchForm.cleaned_data['search'])
        return render(request, 'book/allbooks.html', context)
    return render(request, 'book/allbooks.html', context)


class SearchResultsView(generic.ListView):
    model = Book
    template_name = "book/search_results.html"


    def get_queryset(self):  # new
        query = self.request.GET.get("search")
        if query:
            object_list = Book.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['searched_text'] = self.request.GET.get("search")
        return context

class BooksByAuthorId(generic.ListView):
    model = Book
    template_name = "book/search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("id_field")
        object_list = Book.objects.filter(authors__id=query)#Hrere
        print(f"query==={query}")
        return object_list

    def get_context_data(self, **kwargs):
        context = super(BooksByAuthorId, self).get_context_data(**kwargs)
        context['searched_id'] = self.request.GET.get("id_field")
        return context


def add_book(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BookForm()
            submit = "Add"
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
            submit = "Update"
        context = {'form': form,
                   'submit': submit}
        return render(request, 'book/add_book.html', context)
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/allbooks')


class ID_BookView(generic.DetailView):
    model = Book
    template_name = 'book/id_book.html'


def ordered_books_count_ascending(request):
    book_objects = Book.objects.all().order_by('count')
    # book_objects = Book.objects.filter(count__gt=5) #greater than 5

    context = {'book_objects': book_objects}
    return render(request, 'book/ordered_books.html', context)


def ordered_books_count_descending(request):
    book_objects = Book.objects.all().order_by('-count')

    context = {'book_objects': book_objects}
    return render(request, 'book/ordered_books.html', context)


def ordered_books_name_ascending(request):
    book_objects = Book.objects.all().order_by('name')

    context = {'book_objects': book_objects}
    return render(request, 'book/ordered_books.html', context)


def ordered_books_name_descending(request):
    book_objects = Book.objects.all().order_by('-name')

    context = {'book_objects': book_objects}
    return render(request, 'book/ordered_books.html', context)





