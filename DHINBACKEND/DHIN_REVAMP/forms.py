from django import forms
from .models import Newsletter, CustomUser, Contact, Event, NewsletterSubscriber

# Define the possible choices for the occupation field
OCCUPATION_CHOICES = [
    ('Healthcare Professionals', 'Healthcare Professionals'),
    ('Technology Innovators', 'Technology Innovators'),
    ('Researchers and Academics', 'Researchers and Academics'),
    ('Policy Makers', 'Policy Makers'),
    ('Students and Digital Health Enthusiasts', 'Students and Digital Health Enthusiasts'),
    ('Interns', 'Interns'),
]

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'description', 'date_published', 'content', 'is_active', 'cover_image', 'num_subscribers', 'slug']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'content': forms.Textarea(attrs={'rows': 6, 'cols': 40}),
            'date_published': forms.DateInput(attrs={'type': 'date'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter a slug for the newsletter'}),
        }

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        # You can add custom validation logic for the slug here.
        return slug


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'class': 'form-control'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'message': 'Your Message',
        }


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number', 'occupation']
        widgets = {
            'occupation': forms.Select(choices=OCCUPATION_CHOICES),
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        # If username is not provided, use email as username
        if not username and email:
            cleaned_data['username'] = email
        return cleaned_data
    


    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_published', 'content', 'cover_image']


class NewsletterSubscriberForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']  # Only include the email field
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
        }