from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def wwtp(request):
    return render(request, "wwtp.html")

def school(request):
    return render(request, "school.html")

def tourist(request):
    return render(request, "Tourist.html")
