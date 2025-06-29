def handler(request, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': '{"status": "success", "message": "Vercel deployment is working!", "timestamp": "' + str(__import__("datetime").datetime.now()) + '"}'
    } 