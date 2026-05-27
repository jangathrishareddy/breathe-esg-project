from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("OK - Backend Running")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]