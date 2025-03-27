from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.utils.text import slugify

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_published = models.DateField()
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to='newsletter_covers/', blank=True, null=True)
    num_subscribers = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/newsletters/{self.slug}/"

    class Meta:
        ordering = ['-date_published']


# CONTACT MODEL
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} | {self.first_name} {self.last_name} | {self.phone_number} | {self.occupation}"


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    registration_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/events/{self.id}/"

    class Meta:
        ordering = ['-start_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)  # Ensure the email is unique

    def __str__(self):
        return self.email