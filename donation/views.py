from django.shortcuts import render
from .models import Donator
from django.http import HttpResponse

def donator_list(request):
    d1=Donator.objects.order_by("-donationmade")
    return render(request, 'd_list.html', {'Donators': d1})
    #return HttpResponse("<h2>HEY!</h2>")
# Create your views here.
