from django.contrib import admin
from. models import  Newsletter,  CustomUser,  Contact, Event, NewsletterSubscriber
 
# Register your models here.

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'is_active', 'num_subscribers')
    list_filter = ('is_active', 'date_published')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ('-date_published',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'content')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at',)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'occupation', 'date_joined', 'is_active', 'is_staff')
    list_filter = ('occupation', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

admin.site.register(NewsletterSubscriber)