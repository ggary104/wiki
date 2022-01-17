import random
from django.shortcuts import render, redirect
from .forms import SearchForm, NewForm
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
    if request.method == "GET" and request != "new":
        return render(request, "encyclopedia/entry.html", {
            "form": form,
            "title": entry,
            "content": util.get_entry(entry)
        })


# SEARCH PAGE
def search(request, search):
    form = SearchForm(request.POST)
    entries = util.list_entries()
    for i in range(len(entries)):
        entries[i] = entries[i].lower()
    return render(request, "encyclopedia/search.html", {
        "form": form,
        "search": search.lower(),
        "entries": entries
    })


# NEW PAGE
def new(request):
    form = SearchForm(request.POST)
    newForm = NewForm(request.POST)
    pageExist = False
    if request.method == 'POST' and newForm.is_valid() and util.get_entry(newForm.cleaned_data["title"]) == None:
        open('entries/%s.md' % newForm.cleaned_data["title"], 'x')
        f = open('entries/%s.md' % newForm.cleaned_data["title"], 'a')
        f.write('# %s\n\n' %
                newForm.cleaned_data["title"] + newForm.cleaned_data["content"])
        # f.write('\n')
        # f.write(newForm.cleaned_data["content"])
        f.close()
        return redirect(entry, newForm.cleaned_data["title"])
    elif request.method == 'POST' and newForm.is_valid() and util.get_entry(newForm.cleaned_data["title"]) != None:
        pageExist = True
    return render(request, "encyclopedia/new.html", {
        "pageExist": pageExist,
        "form": form,
        "newForm": newForm,
    })


# RANDOM PAGE
def randomPage(request):
    if request.method == "GET" and request != "new":
        return redirect(entry, random.choice(util.list_entries()))
