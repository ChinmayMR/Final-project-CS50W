from django.contrib.auth.models import AbstractUser
from django.db import models

departments = (
		('HK', 'House keeping'),
		('Accounts', 'Accounts'), 
		('FO', 'Front Office'), 
		('F&B', 'Food and Beverage service'), 
		('General', 'General'), 
  		('Maintence', 'Maintence'), 
        ('Managment', 'Managment'), 
        ('Security', 'Security'), 
	)

complete = (
		('Waiting', 'Waiting'),
		('Rejected', 'Rejected'), 
		('Accepted', 'Accepted'), 
	)

types = (
    ('Sick', 'Sick'),
    ('Casual', 'Casual'),
    ('Privillage', 'Privillage'),
)

class User(AbstractUser):
    approval = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)

class Checklist(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    department = models.CharField(max_length=50, blank=False, null=False, choices=departments)
    
    def __str__(self):
        return f"{self.title} is a checklist with category as {self.department}"
    
class Item(models.Model):
    item = models.CharField(max_length=50)
    checklist = models.ForeignKey("Checklist", on_delete=models.CASCADE, related_name="checklist")

    def __str__(self):
        return f"{self.item} is a part of {self.checklist}"
    
class Alert(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    made_by = models.ForeignKey("User", on_delete=models.CASCADE, related_name="made_by")
    image_url = models.CharField(max_length=255)
    creation_dt = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=50, blank=False, null=False, choices=departments)
    
    def __str__(self):
        return f"Title: {self.title} \n Made by: {self.made_by} \n Creation date: {self.creation_dt} \n Department: {self.department}"
    
class Appointment(models.Model):
    completed = models.CharField(max_length=50, blank=False, null=False, choices=complete)
    complete_msg = models.CharField(max_length=500, blank=True)
    request_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="request_user")
    requested_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="requested_user")
    frm = models.DateTimeField(auto_now=False, auto_now_add=False)
    to = models.DateTimeField(auto_now=False, auto_now_add=False)
    subject = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    
class Leave(models.Model):
    name = models.ForeignKey("User", on_delete=models.CASCADE, related_name="name")
    leave_type = models.CharField(max_length=50, blank=False, null=False, choices=types)
    frm = models.DateTimeField(auto_now=False, auto_now_add=False)
    to = models.DateTimeField(auto_now=False, auto_now_add=False)
    reason = models.CharField(max_length=2000)
    approved = models.CharField(max_length=50, blank=False, null=False, choices=complete)
    approve_msg = models.CharField(max_length=500, blank=True)