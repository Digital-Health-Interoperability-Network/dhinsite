from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Newsletter, CustomUser,  Contact,Event, NewsletterSubscriber
from .serializers import NewsletterSubscriberSerializer, CustomUserSerializer,  ContactSerializer, EventSerializer,  NewsletterSerializer
from django.shortcuts import render,  get_object_or_404, redirect
from .forms import NewsletterForm, ContactForm,CustomUserForm,NewsletterSubscriberForm 
from rest_framework import generics
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
import logging





# Home Page View
def home(request):
    newsletters = Newsletter.objects.all().order_by('-created_at')[:3]  # Get the latest 3 newsletters
    return render(request, 'DHIN_REVAMP/home.html', {'newsletters': newsletters})  # Make sure 'home.html' exists in the templates folder

# search form
def search_results(request):
    query = request.GET.get('q', '')
    newsletters = Newsletter.objects.filter(title__icontains=query) if query else []
    events = Event.objects.filter(title__icontains=query) if query else []
    return render(request, 'DHIN_REVAMP/search_results.html', {
        'query': query,
        'newsletters': newsletters,
        'events': events,
    })
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
class NewsletterListView(ListView):
    model = Newsletter
    template_name = 'DHIN_REVAMP/newsletter_list.html'
    context_object_name = 'newsletters'
    paginate_by = 6  

    def get_queryset(self):
        return Newsletter.objects.filter(is_active=True)

# Detail View for a specific newsletter
class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'DHIN_REVAMP/newsletter_detail.html'
    context_object_name = 'newsletter'

    def get_queryset(self):
        return Newsletter.objects.filter(is_active=True).order_by('-date_published')

# API Viewsets for registration
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



# Traditional views for registration
logger = logging.getLogger(__name__)

def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()  # Saves user without password or username
            messages.success(request, "Registration successful! Welcome to DHIN")
            return redirect('home')  # Redirect to homepage
        else:
            logger.error(f"Form errors: {form.errors}")
            messages.error(request, "Registration failed. Please correct the errors below")
    else:
        form = CustomUserForm()
    
    return render(request, 'DHIN_REVAMP/register_user.html', {'form': form})



# API Viewsets for contactus

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Traditional views for contactus
class ContactView(FormView):
    template_name = 'DHIN_REVAMP/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')  # Redirect after successful form submission

    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent successfully!") 
        return super().form_valid(form)


# API Viewsets for Events

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date_published')
    serializer_class = EventSerializer
    lookup_field = 'slug'

# Traditional views for Events

class EventListView(ListView):
    model = Event
    template_name = 'DHIN_REVAMP/event_list.html'
    context_object_name = 'events'
    ordering = ['-date_published']

class EventDetailView(DetailView):
    model = Event
    template_name = 'DHIN_REVAMP/event_detail.html'
    context_object_name = 'event'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'




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


print("Loading views.py")
