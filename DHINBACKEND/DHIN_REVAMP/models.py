from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Create your models here.


class Newsletter(models.Model):
    # Title of the newsletter
    title = models.CharField(max_length=255)
    
    # Description or summary of the newsletter's content
    description = models.TextField()
    
    # Date of the newsletter issue
    date_published = models.DateField()
    
    # The main body content of the newsletter
    content = models.TextField()

    # Whether the newsletter is active or archived
    is_active = models.BooleanField(default=True)
    
    # An optional field to store the newsletter's cover image
    cover_image = models.ImageField(upload_to='newsletter_covers/', blank=True, null=True)

    # A field to track the number of subscribers (could link to a Subscriber model if needed)
    num_subscribers = models.PositiveIntegerField(default=0)

    # A slug field to create readable URLs for the newsletters
    slug = models.SlugField(unique=True)

    # Creation and update timestamps for the newsletter
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/newsletters/{self.slug}/"

    class Meta:
        ordering = ['-date_published']




class ContactUs(models.Model):
    full_name = models.CharField(max_length=255)  # User's full name
    email = models.EmailField()  # User's email address
    message = models.TextField()  # The actual message sent by the user
    
    

    def __str__(self):
        return f"Contact Us - {self.full_name} ({self.email} {self.message})"

    


    


# Define the possible choices for the occupation field
OCCUPATION_CHOICES = [
    ('Healthcare Professionals', 'Healthcare Professionals'),
    ('Technology Innovators', 'Technology Innovators'),
    ('Researchers and Academics', 'Researchers and Academics'),
    ('Policy Makers', 'Policy Makers'),
    ('Students and Digital Health Enthusiasts', 'Students and Digital Health Enthusiasts'),
    ('Interns', 'Interns'),
]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)  # Unique email address
    username = models.CharField(max_length=30, unique=True)  # Unique username
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    occupation = models.CharField(
        max_length=50, choices=OCCUPATION_CHOICES, blank=True, null=True
    )  # Optional occupation field with choices (dropdown)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # We are using email as the primary identifier for the user
    REQUIRED_FIELDS = ['username']  # Email and username are required fields

    def __str__(self):
         return f"{self.email} | {self.first_name} {self.last_name} | {self.phone_number} | {self.occupation}"



class Event(models.Model):
    # Name of the event
    name = models.CharField(max_length=255)
    
    # Description of the event
    description = models.TextField()
    
    # Date and time when the event starts
    start_date = models.DateTimeField(default=timezone.now)
    
    # Date and time when the event ends
    end_date = models.DateTimeField(default=timezone.now)
    
    # Location where the event is held
    location = models.CharField(max_length=255)
    
    # Optional image for the event (for example, a banner image)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    
    # URL link for event registration or more details
    registration_url = models.URLField(blank=True, null=True)
    
    # Indicates if the event is active or canceled
    is_active = models.BooleanField(default=True)
    
    # Date when the event was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Date when the event was last updated
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # You can customize this to generate a detailed page for each event
        return f"/events/{self.id}/"
    
    class Meta:
        ordering = ['-start_date']  # Orders events by the start date (latest first)