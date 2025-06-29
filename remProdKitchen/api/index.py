import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remProdKitchen.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Create a simple Django app
from django.core.management import execute_from_command_line

def handler(request, context):
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remProdKitchen.settings')
    
    # Import after settings are configured
    from django.core.wsgi import get_wsgi_application
    from django.http import HttpResponse
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static
    
    # Create a simple response for testing
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django on Vercel</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .success { color: green; }
        </style>
    </head>
    <body>
        <h1 class="success">✅ Django is running on Vercel!</h1>
        <p>Your inventory app is successfully deployed.</p>
        <p>Path: {}</p>
        <p>Method: {}</p>
    </body>
    </html>
    """.format(request.get('path', '/'), request.get('method', 'GET'))) 