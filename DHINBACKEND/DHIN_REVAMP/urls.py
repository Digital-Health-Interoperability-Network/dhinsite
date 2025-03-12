from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # ✅ Import views once (no need to import specific functions)
from .views import NewsletterViewSet, CustomUserViewSet, ContactUsViewSet, EventViewSet



# API Router for DRF ViewSets
router = DefaultRouter()
router.register(r'newsletters', NewsletterViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'contacts', ContactUsViewSet)
router.register(r'events', EventViewSet)


urlpatterns = router.urls



urlpatterns = [
    # Basic Pages
    path('', views.home, name='home'),  # Homepage URL
    path('about/', views.about, name='about'),  # About page
    path('dhin-community/', views.dhin_community, name='dhin_community'),
    path('services/', views.services, name='services'),
    path('standards/', views.standards, name='standards'),
    path('global-standards/', views.global_standards, name='global_standards'),
    path('national-standards/', views.national_standards, name='national_standards'),
    path('emeka/', views.emeka, name='emeka'),
    path('julite/', views.julite, name='julite'),
    path('dr-iniobong/', views.dr_iniobong, name='dr_iniobong'),

    
    # Newsletter API Endpoints
    #path('newsletters/', views.newsletter_list, name='newsletter_list'),
    #path('newsletter/<slug:slug>/', views.newsletter_detail, name='newsletter_detail'),
    path('newsletter/create/', views.create_newsletter, name='create_newsletter'),
    path('newsletter/update/<slug:slug>/', views.update_newsletter, name='update_newsletter'),

    # User API Endpoints
    path('register/', views.register_user, name='register_user'),
    path('profile/update/', views.update_profile, name='update_profile'),

    # Event API Endpoints
    path('events/', views.event_list, name='event_list'),
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),

    # Contact API
    path('contact/', views.contact_us_view, name='contact_us_view'),

    # Include Router URLs (if using ViewSets)
    path('api/', include(router.urls)),  # ✅ Ensure router URLs are included
]
