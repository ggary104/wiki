from django.shortcuts import render
from .forms import SearchForm

from . import util


def index(request):
    form = SearchForm(request.POST)
    if request.method == 'GET':
        form = SearchForm(request.POST)
        return render(request, "encyclopedia/index.html", {
            "form": form,
            "entries": util.list_entries()
        })
    elif request.method == 'POST':
        print('test')
        if form.is_valid():
            title = form.cleaned_data["search"],
            print('test2')
            return render(request, "encyclopedia/entry.html", {
                "form": form,
                "title": title[0].capitalize(),
                "content": util.get_entry(title[0])
            })


def entry(request, entry):
    form = SearchForm(request.POST)
    return render(request, "encyclopedia/entry.html", {
        "form": form,
        "title": entry,
        "content": util.get_entry(entry)
    })
