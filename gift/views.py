from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from register.models import Registration, Invitee, Memento


@login_required(login_url="/admin/login/") 
def gift(request):
    """View function for gift page of site."""
    return render(request, 'gift/gift.html')


@login_required(login_url="/admin/login/") 
def search(request):
    """View function for gift search page of site."""
    if request.method == 'POST':
        email = request.POST['email'].lower()
        if not "@" in email:
            email = email + "@ntpc.co.in"

        # Get the status
        try:
            g = Memento.objects.get(registration__invitee__email__iexact = email)
            if g.tag_collected:
                return HttpResponse("Gift collected")
            else:
                return HttpResponse("Gift not collected")
        
        except Memento.DoesNotExist:
            if Registration.objects.filter(invitee__email__iexact = email).exists():
                return HttpResponse("Registration done but gift not issued")
            else:
                return HttpResponse("Not registered")
    
    return HttpResponse("Invalid call")

@login_required(login_url="/admin/login/") 
def issue(request):
    """Issue gift."""
    if request.method == 'POST':
        email = request.POST['email'].lower()
        if not "@" in email:
            email = email + "@ntpc.co.in"

        # Get the status
        try:
            g = Memento.objects.get(registration__invitee__email__iexact = email)
            if g.tag_collected:
                return HttpResponse("Gift collected")
            else:
                return HttpResponse("Gift not collected")
        
        except Memento.DoesNotExist:
            try:
                r = Registration.objects.get(invitee__email__iexact = email)
                m = Memento(
                    registration=r, 
                    tag_collected=True, 
                    issued_to=r.invitee.first_name + " " + r.invitee.last_name, 
                    issued_by=request.user.id
                )
                m.save()
                return HttpResponse("Gift issued")
            
            except Registration.DoesNotExist:
                return HttpResponse("Not registered")
    
    return HttpResponse("Invalid call")