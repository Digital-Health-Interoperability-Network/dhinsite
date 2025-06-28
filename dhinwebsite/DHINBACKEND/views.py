# DHIN_REVAMP/views.py
from django.shortcuts import render

def home(request):
                                          # You can pass context variables to the template if necessary
    return render(request, 'home.html')  # This will render the home.html template
