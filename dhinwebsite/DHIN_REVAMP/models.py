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
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's empty
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Newsletter.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

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
    def create_user(self, email, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()  # No password required
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        user = self.create_user(email, **extra_fields)
        if password:
            user.set_password(password)  # Optional for superusers
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
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
    REQUIRED_FIELDS = []  # No required fields beyond email

    def __str__(self):
        return f"{self.email} | {self.first_name} {self.last_name} | {self.phone_number} | {self.occupation}"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

# EVENT MODEL
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    date_published = models.DateField(default=timezone.now)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Event.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


   #NewsletterSubscriber MODEL
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)  # Ensure the email is unique

    def __str__(self):
        return self.email