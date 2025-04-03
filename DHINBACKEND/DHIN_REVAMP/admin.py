from django.contrib import admin
from. models import  Newsletter, CustomUser, Event, Contact, NewsletterSubscriber
 
# Register your models here.

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'is_active', 'num_subscribers')
    list_filter = ('is_active', 'date_published')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ('-date_published',)
admin.site.register(Event)
admin.site.register(CustomUser)
admin.site.register(Contact)
admin.site.register(NewsletterSubscriber)