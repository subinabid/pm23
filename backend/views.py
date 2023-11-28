from django.shortcuts import render, HttpResponse
from register.models import Invitee

def backend(request):
    """Backend page"""
    return render(request, 'backend/backend.html')

def search(request):
    """Search page"""
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        try:
            invitee = Invitee.objects.get(email__iexact=email)
            return HttpResponse("Invitee found!")

        except Invitee.DoesNotExist:
            return HttpResponse("No such invitee")
    else:
        return HttpResponse("Invalid request")

def add(request):
    """Add page"""
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        try:
            invitee = Invitee.objects.get(email__iexact=email)
            return HttpResponse("Invitee already exists!")

        except Invitee.DoesNotExist:
            return render(request, 'backend/add.html', {'email': email})

    else:
        return HttpResponse("Invalid request")
    
def save(request):
    """Save a new invitee"""
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation = request.POST.get('designation')
        project = request.POST.get('project')
        phone = request.POST.get('phone')
        employee_id = request.POST.get('employee_id')
        # Add
        invitee = Invitee(email=email, first_name=first_name, last_name=last_name, designation=designation, project=project, phone=phone, employee_id=employee_id, invited=True, spot_registered=False)
        invitee.save()
        return HttpResponse("Invitee added!")