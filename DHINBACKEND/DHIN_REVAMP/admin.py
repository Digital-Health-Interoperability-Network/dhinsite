from django.contrib import admin
from. models import  Newsletter, CustomUser, Event, Contact, NewsletterSubscriber
 
# Register your models here.

admin.site.register(Newsletter)
admin.site.register(Event)
admin.site.register(CustomUser)
admin.site.register(Contact)
admin.site.register(NewsletterSubscriber)