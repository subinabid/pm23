"""Views for the venue app."""
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from register.models import Registration, Invitee

@login_required(login_url="/admin/login/")
def venue(request):
    """A view that displays the venue page."""
    return render(request, 'venue/venue.html')


@login_required(login_url="/admin/login/")
def receive(request):
    """A view that displays the venue email page."""
    if request.method == 'POST':
        email = request.POST['email'].lower()
        if not "@" in email:
            email = email + "@ntpc.co.in"

        # Check if the user is registered
        try:
            reg = Registration.objects.get(invitee__email__iexact=email)
            if reg.arrival_at_venue:
                pass
            else:
                reg.arrival_at_venue =  datetime.now() # mark as arrived
                reg.save()
            return render(request, 'venue/view.html', {'registered': reg})
        
        except Registration.DoesNotExist:
            return HttpResponse("You are not registered")
    
    return HttpResponse("Invalid call")


@login_required(login_url="/admin/login/")
def undo(request, id):
    """A view that undoes the arrival at venue."""
    try:
        reg = Registration.objects.get(id=id)
        reg.arrival_at_venue = None
        reg.save()
        return redirect('venue')
    except Registration.DoesNotExist:
        return HttpResponse("Invalid call")
    

@login_required(login_url="/admin/login/")
def search(request):
    """A view that searches for a status."""
    if request.method == 'POST':
        email = request.POST['email'].lower()
        if not "@" in email:
            email = email + "@ntpc.co.in"

        # Get the status
        try:
            reg = Registration.objects.get(invitee__email__iexact = email)
            if reg.arrival_at_venue:
                return HttpResponse("Arrived")
            else:
                return HttpResponse("Registered, Not arrived")
        
        except Registration.DoesNotExist:
            return HttpResponse("Not registered")
    
    return HttpResponse("Invalid call")

@login_required(login_url="/admin/login/")
def reports(request):
    """A view that displays the venue reports page."""
    context = {
        'invited': Invitee.objects.filter(invited=True).count(),
        'invited_self': Invitee.objects.filter(invited=False).count(),
        'invited_total': Invitee.objects.all().count(),
        'registered_inv': Registration.objects.filter(invitee__invited=True).count(),
        'registered_self': Registration.objects.filter(invitee__invited=False).count(),
        'registered_all': Registration.objects.all().count(),
        'arrived_inv': Registration.objects.filter(invitee__invited=True, arrival_at_venue__isnull=False).count(),
        'arrived_self': Registration.objects.filter(invitee__invited=False, arrival_at_venue__isnull=False).count(),
        'arrived_all': Registration.objects.filter(arrival_at_venue__isnull=False).count(),
    }
    return render(request, 'venue/reports.html', context)