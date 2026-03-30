from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'newApp/about.html')

def contact(request):
    return render(request, 'newApp/contact.html')

def services(request):
    return render(request, 'newApp/app.html')