from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "testsite/index.html")

def me(request):
    return HttpResponse("This is me!")

def dynamo(request, customtext):
    return render(request, "testsite/mycust.html", {
        "cust": customtext.upper()
    })

def dynamo2(request):
    customtext = "rubbish"
    return render(request, "testsite/mycust.html", {
        "cust": customtext.upper()
    })
