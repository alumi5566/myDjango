from django.http import HttpResponse
from django.template import loader

def base(request):
    #     return render(request, "home/index.html")
    #     return HttpResponse("You're looking at home.")
    template = loader.get_template("home/base.html")
    return HttpResponse(template.render(None, request))