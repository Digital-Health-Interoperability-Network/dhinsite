from django.contrib import admin
from. models import  Newsletter, CustomUser, Event, ContactUs
 
# Register your models here.

admin.site.register(Newsletter)
admin.site.register(Event)
admin.site.register(CustomUser)
admin.site.register(ContactUs)