from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render

def HomeView(request):
    return render(request, 'home.html')

def BookTableView(request):
    return render(request, 'book_table.html')

def MenuView(request):
    return render(request, 'menu.html')

def AboutView(request):
    return render(request, 'about.html')

def FeedbackView(request):
    return render(request, 'feedback.html')
