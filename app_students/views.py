from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def ce01s(request):
    return render(request, 'app_students/ce01s.html')
def ce02s(request):
    return render(request, 'app_students/ce02s.html')
def ce03s(request):
    return render(request, 'app_students/ce03s.html')
def ce04s(request):
    return render(request, 'app_students/ce04s.html')