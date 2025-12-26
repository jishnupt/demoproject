from django.shortcuts import render
from .forms import Registeruser
from .models import MainEvents

# Create your views here.
def homepage(request):
    event_m = MainEvents.objects.all()
    return render(request,'home.html',{'event_m':event_m})

def aboutpage(request):
    return render(request,'about.html')

def registration(request):
    form = Registeruser()
    return render(request,'reg.html',{'form':form})
