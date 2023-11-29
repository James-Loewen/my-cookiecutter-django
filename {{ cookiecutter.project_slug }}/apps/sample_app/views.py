from django.shortcuts import render


def index(request):
    template_name = "sample_app/index.html"
    context = {"name": "Suki"}
    return render(request, template_name, context)
