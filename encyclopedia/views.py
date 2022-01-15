from django.shortcuts import render, redirect
from .forms import SearchForm

from . import util


# INDEX PAGE
def index(request):
    form = SearchForm(request.POST)
    if request.method == 'GET':
        return render(request, "encyclopedia/index.html", {
            "form": form,
            "entries": util.list_entries()
        })
    # -> FROM LINK
    elif request.method == 'POST' and form.is_valid() and util.get_entry(form.cleaned_data["search"]) != None:
        return redirect(entry, form.cleaned_data["search"])
    # -> FROM SEARCH
    elif request.method == 'POST' and form.is_valid() and util.get_entry(form.cleaned_data["search"]) == None:
        return redirect(search, form.cleaned_data["search"])


# ENTRY PAGE
def entry(request, entry):
    form = SearchForm(request.POST)
    if request.method == "GET":
        return render(request, "encyclopedia/entry.html", {
            "form": form,
            "title": entry,
            "content": util.get_entry(entry)
        })

# SEARCH PAGE


def search(request, search):
    form = SearchForm(request.POST)
    print(search)
    return render(request, "encyclopedia/search.html", {
        "form": form,
        "search": search,
        "entries": util.list_entries()
    })
