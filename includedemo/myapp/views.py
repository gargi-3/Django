from django.shortcuts import render

# Create your views here.
def home(request):
    nav_links=[
        {'name': 'Home', 'url': '/'},
        {'name': 'Aboutus', 'url': '/aboutus/'},
        {'name': 'Contact', 'url': '/contact/'}
    ]

    context = {
        'nav_links': nav_links
    }

    return render(request, 'myapp/base.html', context)