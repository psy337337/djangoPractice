from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'siteApp/main.html')

def seventeen(request):
    return render(request,'siteApp/seventeen.html')

def apink(request):
    return render(request,'siteApp/apink.html')

def lostark(request):
    return render(request,'siteApp/lostark.html')
