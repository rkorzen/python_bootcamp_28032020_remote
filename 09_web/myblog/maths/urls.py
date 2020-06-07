from django.urls import path

from maths.views import add, mul, div, sub, list_example

urlpatterns = [
    path("div/<int:a>/<int:b>", div),
    path("add/<int:a>/<int:b>", add),
    path("sub/<int:a>/<int:b>", sub),
    path("mul/<int:a>/<int:b>", mul),
    path("list_example/", list_example)
]