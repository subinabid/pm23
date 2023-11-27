
from django.shortcuts import render, redirect, HttpResponse
from .models import Invitee, Registration


def register(request):
    """View function for registration app home page."""
    return render(request, 'register/register.html')


def email(request):
    """Check if the email is valid."""
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        try: 
            # registered = True
            reg =  Registration.objects.get(invitee__email__iexact = email)
            return redirect('register_view', id=reg.id)  

        except Registration.DoesNotExist:
            # registered = False, invited = True
            try:
                invitee = Invitee.objects.get(email__iexact = email)
                return render(request, 'register/invited.html', {'invitee': invitee})

            except Invitee.DoesNotExist:
                # Registered = False, invited = False
                return render(request, 'register/new.html', {'email': email})
        
    else:
        return HttpResponse("Invalid call")
    
def new(request):
    """Create a new registration."""
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation = request.POST.get('designation')
        location = request.POST.get('location')
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')
        # Add to invitees list with invited=False
        invitee = Invitee(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            designation=designation, 
            project=location, 
            invited=False
        )
        invitee.save()
        # Add to registrations list
        reg = Registration(
            invitee=invitee, 
            arrival_date=arrival_date, 
            departure_date=departure_date
        )
        reg.save()
        return redirect('register_view', id=reg.id)
        
    else:
        return HttpResponse("Invalid call")

def invited(request):
    """Create a new registration."""
    if request.method == 'POST':
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')

        # Add to registrations list
        reg = Registration(
            invitee=Invitee.objects.get(email__iexact = request.POST.get('email').lower()), 
            arrival_date=arrival_date, 
            departure_date=departure_date
        )
        reg.save()
        return redirect('register_view', id=reg.id)
    
    else:
        return HttpResponse("Invalid call")
    
def view(request, id):
    """View registration detail."""
    try:
        reg = Registration.objects.get(id=id)
        return render(request, 'register/view.html', {'registered': reg})
    except Registration.DoesNotExist:
        return HttpResponse("Invalid id")