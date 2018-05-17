from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "model_store/index.html", context)
