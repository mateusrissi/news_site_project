from django.http import HttpResponse
from django.shortcuts import render

def news_view(request):
    return render(request, 'index.html')
