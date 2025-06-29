import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remProdKitchen.settings')

# Import Django components
import django
django.setup()

from django.core.wsgi import get_wsgi_application
from django.test import RequestFactory
from django.http import HttpResponse

# Create WSGI application
application = get_wsgi_application()

def handler(request, context):
    """Django handler for Vercel serverless function"""
    try:
        # Convert Vercel request to Django request
        factory = RequestFactory()
        
        # Get request data
        method = request.get('method', 'GET')
        path = request.get('path', '/')
        headers = request.get('headers', {})
        body = request.get('body', '')
        
        # Create Django request
        django_request = factory.generic(
            method=method,
            path=path,
            data=body,
            content_type=headers.get('content-type', 'text/plain')
        )
        
        # Add headers
        for key, value in headers.items():
            django_request.META[f'HTTP_{key.upper().replace("-", "_")}'] = value
        
        # Process request through Django
        response = application(django_request, lambda *args: None)
        
        # Convert Django response to Vercel response
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.content.decode('utf-8') if hasattr(response, 'content') else str(response)
        }
        
    except Exception as e:
        # Return error response
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html'},
            'body': f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Django Error</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .error {{ color: red; }}
                    .info {{ color: blue; }}
                </style>
            </head>
            <body>
                <h1 class="error">Django Error</h1>
                <p class="info">Error: {str(e)}</p>
                <p>Django integration is being set up. Please try the simple version first.</p>
            </body>
            </html>
            '''
        } 