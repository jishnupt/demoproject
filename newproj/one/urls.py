from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home',homepage),
    path('about',aboutpage),
    path('Registration',registration),
    path('eventbooking/<int:eid>',book_event,name='book_event'),
    path('allevents/<int:pid>',allevents,name='allevents'),
    path('booked_evnts',booked_evnts,name='booked_evnts')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

