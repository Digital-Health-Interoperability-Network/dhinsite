from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Newsletter, CustomUser, Event, ContactUs
from .serializers import NewsletterSerializer, CustomUserSerializer, EventSerializer, ContactUsSerializer
from django.shortcuts import render,  get_object_or_404, redirect
from .forms import NewsletterForm
from rest_framework.decorators import action
from django.templatetags.static import static

from django.shortcuts import render
from django.http import HttpResponse






# Home Page View
def home(request):
    return render(request, 'DHIN_REVAMP/Homepage.html')  # Make sure 'home.html' exists in the templates folder

# About Page View
def about(request):
    return render(request, 'DHIN_REVAMP/AboutDHIN.html')

# DHIN Community Page
def dhin_community(request):
    return render(request, 'DHIN_REVAMP/DHINcommunity.html')

# Services Page
def services(request):
    return render(request, 'DHIN_REVAMP/Servicepage.html')

# Standards Page
def standards(request):
    return render(request, 'DHIN_REVAMP/Standards.html')

# Global Standards Page
def global_standards(request):
    return render(request, 'DHIN_REVAMP/Globalstandards.html')

# National Standards Page
def national_standards(request):
    return render(request, 'DHIN_REVAMP/Nationalstandards.html')

# Emeka Page
def emeka(request):
    return render(request, 'DHIN_REVAMP/Emekapage.html')

# Julite Page
def julite(request):
    return render(request, 'DHIN_REVAMP/juliet.html')

# Dr. Iniobong Page
def dr_iniobong(request):
    return render(request, 'DHIN_REVAMP/Driniobong.html')


# API Viewsets for newsletter

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    @action(detail=True, methods=['get'])
    def get_newsletter_detail(self, request, pk=None):
        newsletter = self.get_object()
        return Response(NewsletterSerializer(newsletter).data)


# Traditional views for newsletter

def create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('newsletter_list')  # Redirect after creation
    else:
        form = NewsletterForm()

    return render(request, 'DHIN_REVAMP/Newsletter.html', {'form': form, 'action': 'Create'})

def update_newsletter(request, slug):
    newsletter = get_object_or_404(Newsletter, slug=slug)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES, instance=newsletter)
        if form.is_valid():
            form.save()
            return redirect(newsletter.get_absolute_url())  # Redirect to detail page
    else:
        form = NewsletterForm(instance=newsletter)

    return render(request, 'DHIN_REVAMP/Newsletter.html', {'form': form, 'action': 'Update', 'newsletter': newsletter})

def newsletter_list(request):
    newsletters = Newsletter.objects.all()  # Query all newsletters
    return render(request, 'DHIN_REVAMP/Newsletter.html', {'newsletters': newsletters})




# API Viewsets for registration
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]



# Traditional views for registration
def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('profile')  # Redirect after registration
    else:
        form = CustomUserForm()

    return render(request, 'DHIN_REVAMP/Registration.html', {'form': form})


def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect after update
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'DHIN_REVAMP/Registration.html', {'form': form})





# API Viewsets for contactus

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def submit_contact_message(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Return 201 if created
        return Response(serializer.errors, status=400)  # Return errors if invalid



# Traditional views for contactus

def contact_us_view(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  # Save contact message
            return redirect('Successful')  # Redirect after submission
    else:
        form = ContactUsForm()

    return render(request, 'DHIN_REVAMP/ContactUs.html', {'form': form})





# API Viewsets for Events


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventSerializer

    @action(detail=True, methods=['get'])
    def get_event_detail(self, request, pk=None):
        event = self.get_object()
        return Response(EventSerializer(event).data)



# Traditional views for Events

def event_list(request):
    events = Event.objects.filter(is_active=True)
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'DHIN_REVAMP/Events.html', {'event': event})
