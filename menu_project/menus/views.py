from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "index.html")


def team(request):
    return render(request, "index.html")


def service(request):
    return render(request, "index.html")


def web(request):
    return render(request, "index.html")


def seo(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "index.html")
