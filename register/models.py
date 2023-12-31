from django.db import models

class Invitee(models.Model):
    """Model representing an invitee."""
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=25)
    project = models.CharField(max_length=40)
    invited = models.BooleanField(default=True)
    spot_registered = models.BooleanField(default=False)
    pm_dept = models.BooleanField(default=False)
    vendor = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, null=True, blank=True)
    employee_id = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.email}'

class Registration(models.Model):
    """Model representing a registration."""
    invitee = models.ForeignKey('Invitee', on_delete=models.CASCADE)
    registration_date = models.DateField(null=True, blank=True, auto_now_add=True)
    arrival_date = models.DateField(null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    arrival_at_venue = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.invitee}'

class Memento(models.Model):
    """Model representing a memento."""
    registration = models.ForeignKey('Registration', on_delete=models.CASCADE)
    tag_generated = models.BooleanField(default=False)
    tag_printed = models.BooleanField(default=False)
    tag_collected = models.BooleanField(default=False)
    issued_to = models.CharField(max_length=100, null=True, blank=True)
    issued_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.registration}'
