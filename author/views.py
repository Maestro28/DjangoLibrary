from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q

from author.models import Author
from author.forms import AuthorForm, SearchingAuthorForm


# Create your views here.

def all_authors(request):
    author_objects = Author.objects.all()
    form = SearchingAuthorForm()

    context = {'author_objects': author_objects,
               'form': form,
               }
    return render(request, 'author/all_authors.html', context)

def add_author(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AuthorForm()
            submit = "Add"
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(instance=author)
            submit = "Update"
        context = {'form': form,
                   'submit': submit}
        return render(request, 'author/add_author.html', context)
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/authors/all_authors')


class SearchResultsView(generic.ListView):
    model = Author
    template_name = "author/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            object_list = Author.objects.filter(
                Q(name__icontains=query) | Q(surname__icontains=query)
            )
            return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['searched_text'] = self.request.GET.get("search")
        return context
