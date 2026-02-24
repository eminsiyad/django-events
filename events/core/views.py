from django.shortcuts import render,get_object_or_404, redirect
from .models import Event, Registration
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def event_list(request):
    events = Event.objects.filter(date__gte = timezone.now())
    return render(request,'event_list.html', {'events':events})

def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request,'event_details.html', {'event' : event})

@login_required
def register_event(request,pk):
    event = get_object_or_404(Event, pk=pk)
    if event.registration_set.count() >= event.max_participants:
        messages.error(request, "event is full.")
        return redirect('event_details', pk=pk)
    if Registration.objects.filter(user = request.user, event=event).exists():
        messages.error(request, 'you already registred for this event.')
        return redirect('event_details', pk=pk)
    
    Registration.objects.create(user=request.user, event=event)
    messages.success(request,"successfully registered.")
    return redirect('my_events')

@login_required
def my_events(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'my_events.html', {'registrations' : registrations})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})
