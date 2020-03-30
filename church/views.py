from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def volunteer(request):
    return render(request, 'volunteer.html')


def contact(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'about.html')

