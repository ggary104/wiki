from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search/<str:search>", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("random/", views.randomPage, name="randomPage"),
    path("edit/<str:edit>", views.edit, name="edit")
]
