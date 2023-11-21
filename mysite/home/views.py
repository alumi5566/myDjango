from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

def base(request):
#     return render(request, "home/index.html")
#     return HttpResponse("You're looking at home.")
    template = loader.get_template("home/base.html")
    return HttpResponse(template.render(None, request))
