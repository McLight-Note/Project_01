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
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Create WSGI application
application = get_wsgi_application()

def handler(request, context):
    """Simple Vercel serverless function handler"""
    try:
        # Get request info
        method = request.get('method', 'GET')
        path = request.get('path', '/')
        
        # Return a simple working response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Inventory Management System</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    body {{ padding: 20px; }}
                    .success {{ color: green; }}
                    .info {{ color: blue; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-md-8">
                            <div class="card">
                                <div class="card-header">
                                    <h1 class="text-center success">✅ Vercel Deployment Successful!</h1>
                                </div>
                                <div class="card-body">
                                    <h3>Your Inventory Management System is Live</h3>
                                    <p class="info"><strong>Request Method:</strong> {method}</p>
                                    <p class="info"><strong>Request Path:</strong> {path}</p>
                                    
                                    <hr>
                                    
                                    <h4>Features Available:</h4>
                                    <ul>
                                        <li>✅ Product Management (Add, Edit, Delete)</li>
                                        <li>📱 Mobile Responsive Design</li>
                                        <li>🖼️ Image Upload Support</li>
                                        <li>📊 Quantity Management</li>
                                        <li>📁 Data Export/Import</li>
                                        <li>💾 Backup System</li>
                                    </ul>
                                    
                                    <hr>
                                    
                                    <h4>Next Steps:</h4>
                                    <p>The serverless function is working correctly. Django integration is being set up.</p>
                                    
                                    <div class="alert alert-info">
                                        <strong>Note:</strong> This is a test page. The full Django application will be available once the integration is complete.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            </body>
            </html>
            '''
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
                <title>Server Error</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .error {{ color: red; }}
                </style>
            </head>
            <body>
                <h1 class="error">Server Error</h1>
                <p>Error: {str(e)}</p>
                <p>Please try again later or contact support.</p>
            </body>
            </html>
            '''
        } 