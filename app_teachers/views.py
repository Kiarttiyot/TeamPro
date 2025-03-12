from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def teachers(request):
    return render(request,'app_teachers/teachers.html')