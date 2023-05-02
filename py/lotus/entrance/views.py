from django.shortcuts import render

def index(request):
    return render(request, 'entrance/index.html')

def about(request):
    return render(request, 'entrance/about.html')

def breathe(request):
    return render(request, 'entrance/breathe.html')

def entr(request):
    return render(request, 'entrance/entr.html')

def nature(request):
    return render(request, 'entrance/nature.html')