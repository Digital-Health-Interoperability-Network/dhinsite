from rest_framework import serializers
from .models import Newsletter, CustomUser, Event, ContactUs

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'title', 'description', 'date_published', 'content', 'is_active', 'cover_image', 'num_subscribers', 'slug']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'occupation', 'date_joined', 'is_active']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'is_active']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'full_name', 'email', 'message']
