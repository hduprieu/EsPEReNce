from django.shortcuts import render

# Create your views here.
def index(request,message="Welcome to esPEReNce!"):
    message = "Welcome to esPEReNce!"
    sources = [
        {
            'name': 'Source 1',
            'url': 'https://www.djangoproject.com/',
            'description': 'The web framework for perfectionists with deadlines.',
        },
        {
            'name': 'Source 2',
            'url': 'https://www.python.org/',
            'description': 'Python is a programming language that lets you work quickly and integrate systems more effectively.',
        },
        {
            'name': 'Source 3',
            'url': 'https://git-scm.com/',
            'description': 'Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.',
        },
    ]
    return render(request, 'index.html', {'message': message, 'sources': sources})