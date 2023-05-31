from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Checklist)
admin.site.register(Item)
admin.site.register(Alert)
admin.site.register(Appointment)
admin.site.register(Leave)