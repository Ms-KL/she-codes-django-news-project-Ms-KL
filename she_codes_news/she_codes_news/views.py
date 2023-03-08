
from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('news/')
    return response

# Resource: https://realpython.com/django-redirects/#django-redirects-a-super-simple-example