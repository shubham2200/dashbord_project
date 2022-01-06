from django.shortcuts import render

# Create your views here.


def dashbord(request):
    return render(request, 'dashbord.html')

def products(request):
    return render(request, 'products.html')

def costomer(request):
    return render(request, 'costomer.html')