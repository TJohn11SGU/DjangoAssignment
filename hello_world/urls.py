from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # ✅ Add this import

# ✅ Define a simple home view
def home(request):
    return HttpResponse("Welcome to the Hello World Django app!")

urlpatterns = [
    path('', home),  # ✅ Add this line to handle '/'
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
]
