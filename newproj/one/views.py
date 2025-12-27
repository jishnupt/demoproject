from django.shortcuts import render,redirect
from .forms import Registeruser,EventBookingForm
from .models import MainEvents,Events,EventBooking

# Create your views here.
def homepage(request):
    event_m = MainEvents.objects.all()
    return render(request,'home.html',{'event_m':event_m})

def allevents(request,pid):
    eventt = Events.objects.filter(main_event=pid)
    return render(request,'allevent.html',{'eventt':eventt})

def aboutpage(request):
    return render(request,'about.html')

def registration(request):
    form = Registeruser()
    return render(request,'reg.html',{'form':form})

def booked_evnts(request):
    bookd_e = EventBooking.objects.all()
    return render(request,'booked_evn.html',{'bookd_e':bookd_e})


def book_event(request,eid):
    evnt = Events.objects.get(id=eid)
    if request.method == 'POST':
        form = EventBookingForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.name = evnt
            data.save()
            return redirect(homepage)
    else:
        form = EventBookingForm()

    return render(request, 'book_event.html', {'form': form})

