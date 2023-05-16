from django.shortcuts import render

def index(request):
    return render(request, 'entrance/index.html')

def about(request):
    return render(request, 'entrance/about.html')

def breathe(request):
    return render(request, 'entrance/breathe.html')

def entr(request):
    return render(request, 'entrance/entr.html')

def reg(request):
    return render(request, 'entrance/reg.html')

def nature(request):
    return render(request, 'entrance/nature.html')

def space(request):
    return render(request, 'entrance/space.html')
def asmr(request):
    return render(request, 'entrance/asmr.html')
def lofi(request):
    return render(request, 'entrance/lofi.html')
def whitenoise(request):
    return render(request, 'entrance/whitenoise.html')