from django.urls import path

from maths.views import add, mul, div, sub

urlpatterns = [
    path("div/<int:a>/<int:b>", div),
    path("add/<int:a>/<int:b>", add),
    path("sub/<int:a>/<int:b>", sub),
    path("mul/<int:a>/<int:b>", mul),
]