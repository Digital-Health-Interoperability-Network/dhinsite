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
from django.views.generic import ListView, DetailView






# Home Page View
def home(request):
    newsletters = Newsletter.objects.all().order_by('-created_at')[:3]  # Get the latest 3 newsletters
    return render(request, 'DHIN_REVAMP/Homepage.html', {'newsletters': newsletters})  # Make sure 'home.html' exists in the templates folder


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


