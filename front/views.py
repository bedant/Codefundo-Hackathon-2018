from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'fronthome.html')
def about_us(request):
    return render(request, 'about_us.html')
def contact_us(request):
    return render(request, 'contact.html')
def victim(request):
    return render(request, 'victim.html')
def volunteer(request):
    return render(request, 'volunteer.html')
def donationbig(request):
    return render(request, 'frontdonationnew.html')
def bankportal(request):
    return render(request,'Bankportal.html')