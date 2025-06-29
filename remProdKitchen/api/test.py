def handler(request, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Vercel Test</title>
        </head>
        <body>
            <h1>✅ Vercel Deployment Working!</h1>
            <p>Your Django app is successfully deployed on Vercel.</p>
            <p>Now you can access your inventory app at the main URL.</p>
        </body>
        </html>
        '''
    } 