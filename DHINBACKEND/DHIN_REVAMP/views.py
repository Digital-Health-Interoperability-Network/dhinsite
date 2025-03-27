from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Newsletter, CustomUser, Event, Contact, NewsletterSubscriber
from .serializers import NewsletterSubscriberSerializer, CustomUserSerializer, EventSerializer, ContactSerializer,  NewsletterSerializer
from django.shortcuts import render,  get_object_or_404, redirect
from .forms import NewsletterForm, ContactForm,CustomUserForm,NewsletterSubscriberForm 
from rest_framework.decorators import action
from django.templatetags.static import static
from rest_framework import generics
from django.http import JsonResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View






# Home Page View
def home(request):
    return render(request, 'DHIN_REVAMP/Homepage.html')  # Make sure 'home.html' exists in the templates folder

# About Page View
def about(request):
    return render(request, 'DHIN_REVAMP/about.html')

# DHIN Community Page
def dhin_community(request):
    return render(request, 'DHIN_REVAMP/dhin_community.html')

# Services Page
def services(request):
    return render(request, 'DHIN_REVAMP/services.html')

# Standards Page
def standards(request):
    return render(request, 'DHIN_REVAMP/standards.html')

# Global Standards Page
def global_standards(request):
    return render(request, 'DHIN_REVAMP/global_standards.html')

# National Standards Page
def national_standards(request):
    return render(request, 'DHIN_REVAMP/national_standards.html')

# Emeka Page
def emeka(request):
    return render(request, 'DHIN_REVAMP/emeka.html')

# Julite Page
def julite(request):
    return render(request, 'DHIN_REVAMP/julite.html')

# Dr. Iniobong Page
def dr_iniobong(request):
    return render(request, 'DHIN_REVAMP/dr_iniobong.html')


# API Viewsets for newsletter

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


# Traditional views for newsletter

# List all newsletters
def newsletter_list(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'DHIN_REVAMP/newsletter_list.html', {'newsletters': newsletters})

# View a specific newsletter
def newsletter_detail(request, slug):
    newsletter = get_object_or_404(Newsletter, slug=slug)
    return render(request, 'DHIN_REVAMP/newsletter_detail.html', {'newsletter': newsletter})

# Create a new newsletter
def newsletter_create(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('newsletter_list')  # Redirect to the newsletter list view
    else:
        form = NewsletterForm()
    return render(request, 'DHIN_REVAMP/newsletter_create.html', {'form': form})

# Update an existing newsletter
def newsletter_update(request, slug):
    newsletter = get_object_or_404(Newsletter, slug=slug)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES, instance=newsletter)
        if form.is_valid():
            form.save()
            return redirect('newsletter_detail', slug=newsletter.slug)
    else:
        form = NewsletterForm(instance=newsletter)
    return render(request, 'DHIN_REVAMP/newsletter_update.html', {'form': form})

# Delete a newsletter
def newsletter_delete(request, slug):
    newsletter = get_object_or_404(Newsletter, slug=slug)
    if request.method == 'POST':
        newsletter.delete()
        return redirect('newsletter_list')
    return render(request, 'DHIN_REVAMP/newsletter_delete.html.html', {'newsletter': newsletter})



# API Viewsets for registration
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



# Traditional views for registration
class CustomUserListView(View):
    def get(self, request):
        form = CustomUserForm()
        users = CustomUser.objects.all()
        return render(request, 'DHIN_REVAMP/register_user.html', {'users': users})
def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('user_list')  # Redirect to user list or another page after successful registration
    else:
        form = CustomUserForm()
    
    return render(request, 'DHIN_REVAMP/register_user.html', {'form': form})  # Render the registration template




# API Viewsets for contactus

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Traditional views for contactus
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or success page
    else:
        form = ContactForm()
    return render(request, 'DHIN_REVAMP/contact.html', {'form': form})




# API Viewsets for Events


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Traditional views for Events

class EventListView(View):
       def get(self, request):
           events = Event.objects.all()
           return render(request, 'DHIN_REVAMP/event.html', {'events': events})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event.html', {'event': event})



class NewsletterSubscriberCreateView(generics.CreateAPIView):
       queryset = NewsletterSubscriber.objects.all()
       serializer_class = NewsletterSubscriberSerializer

# Traditional views for subscriber
def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Successfully subscribed!'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid email. Please try again.'}, status=400)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


