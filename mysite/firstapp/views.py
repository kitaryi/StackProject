from django.shortcuts import render


def pages_page(request):
    return render(request, 'page.html')
# Create your views here.
