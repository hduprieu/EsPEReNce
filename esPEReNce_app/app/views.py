from django.shortcuts import render
from django.http import HttpResponse
import sys

# Create your views here.
def index(request):
    # Default message
    message = "Welcome to esPEReNce !"
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

    # Check if the form has been submitted
    if request.method == 'POST':
        # Get the search query from the form
        search_query = request.POST.get('search', None)  # Default to None if 'search' key doesn't exist
        if search_query:
            # Print the search query to the console
            print(f"Search query: {search_query}", file=sys.stderr)
            # You can also modify the message or perform a search operation here
            message = f"Results for: {search_query}"
        else:
            message = "No search query provided."

    return render(request, 'index.html', {'message': message, 'sources': sources})
