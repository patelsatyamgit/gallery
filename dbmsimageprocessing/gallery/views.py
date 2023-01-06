from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import Books

# Create your views here.
def greetings(request):
    bb=Books.objects.all()
    for i in bb:
       return render(request,'gallery/greeting.html',{'bb':bb});
