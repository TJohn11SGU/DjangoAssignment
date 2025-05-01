from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Add this import for redirection

# Define a simple home view that redirects to /polls/
def home(request):
    return redirect('/polls/')  # Redirect to /polls/

urlpatterns = [
    path('', home),  # Redirect root URL (/) to /polls/
    path("polls/", include("polls.urls")),  # Polls app at /polls/
    path('admin/', admin.site.urls),
]
