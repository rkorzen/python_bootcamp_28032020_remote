"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse




def hello(request, name=""):
    greetings = "Hello " + name.upper()
    return HttpResponse(greetings)


def hello2(request, number):
    print("Wpadatu")
    return HttpResponse(f"Square: {number ** 2}")


urlpatterns = [
    path('admin/', admin.site.urls),

    path("", lambda x: HttpResponse("Welcome on my Blog")),
    path("hello/", hello),
    path("hello/<int:number>", hello2),
    path("hello/<name>", hello),

    path("math/", include("maths.urls")),
]
