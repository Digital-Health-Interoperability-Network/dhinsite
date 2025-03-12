from django import forms
from .models import Newsletter, CustomUser, OCCUPATION_CHOICES
from .models import ContactUs 


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'description', 'date_published', 'content', 'is_active', 'cover_image', 'num_subscribers', 'slug']

        # If you want to specify custom widgets or labels for any fields, you can do so here.
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




       
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'message']
    
                                                                        # You can also add custom labels, widgets, or validation if needed
    full_name = forms.CharField(label='Full Name', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Write your message here', 'rows': 5}))



    



class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number', 'occupation']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data







