from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        return render(request, 'lk/index.html')