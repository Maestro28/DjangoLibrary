from django.shortcuts import render, redirect
from author.models import Author, AuthorForm

# Create your views here.

def all_authors(request):
    author_objects = Author.objects.all()

    context = {'author_objects': author_objects,
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