from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # ✅ Import views once (no need to import specific functions)
from .views import NewsletterViewSet, CustomUserViewSet,   NewsletterSubscriberCreateView, ContactViewSet
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    NewsletterDetailView, NewsletterListView,
    ContactView,
    EventListView, EventDetailView, EventViewSet,
    subscribe_newsletter,
    register_user,
   
    
    
)

# API Router for DRF ViewSets
router = DefaultRouter()
router.register(r'newsletters', views.NewsletterViewSet)
router.register(r'users', views.CustomUserViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'contacts', views.ContactViewSet)


urlpatterns = [
        # DRF API Router
    path('api/', include(router.urls)),
    
    
    # Basic Pages
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('about/', views.about, name='about'),
    path('dhin-community/', views.dhin_community, name='dhin_community'),
    path('services/', views.services, name='services'),
    path('standards/', views.standards, name='standards'),
    path('global-standards/', views.global_standards, name='global_standards'),
    path('national-standards/', views.national_standards, name='national_standards'),
    path('emeka/', views.emeka, name='emeka'),
    path('julite/', views.julite, name='julite'),
    path('dr-iniobong/', views.dr_iniobong, name='dr_iniobong'),
    

    # Newsletter Traditional Views
    path('newsletters/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletters/<slug:slug>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    # Users
    
    path('users/register/', register_user, name='register_user'),

    # Events
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<slug:slug>/', EventDetailView.as_view(), name='event_detail'),

    # Contact Us
    
     path('contact/', ContactView.as_view(), name='contact'),

    # URL for the newsletter subscription form
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
    
    ]


