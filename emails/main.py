from flask import abort


def get_bearer_token(request):
    bearer_token = request.headers['Authorization', None]
    if not bearer_token:
        abort(401)
    parts = bearer_token.split()
    if parts[0].lower() != "bearer":
        # Authorization header must start with bearer
        abort(401)
    elif len(parts) == 1:
        # Token was not found
        abort(401)
    elif len(parts) > 2:
        # authorization header must be of the form 'Bearer token'
        abort(401)
    bearer_token = parts[1]
    return bearer_token


def send_mail(sender,receiver,subject,message):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    #if request.method != 'POST':
    #    abort(405)
    # bearer_token = request.headers['Authorization'].split()[1]
    #bearer_token = get_bearer_token(request)
    #secret_key = os.environ.get('ACCESS_TOKEN')
    #if bearer_token != secret_key:
    #    abort(401)
#     sender = request_json['sender']
#     receiver = request_json['receiver']
#     subject = request_json['subject']
#     message = request_json['message']
   # request_json = request.get_json(silent=True)
    #parameters = ('sender', 'receiver', 'subject', 'message')
#     sender, receiver, subject, message = '', '', '', ''
#     if request_json and all(k in request_json for k in parameters):
#         sender = sender
#         receiver = receiver
#         subject = subject
#         message = message
#     else:
#         abort(400)
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=message
    )
    return
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
        return 'OK', 200

    except Exception as e:
        return e, 400

send_mail(sender= "santusub4u@gmail.com",receiver= "katkuri.santhosh@gmail.com",subject= "Testing for new cloud function to send email",message= "Hi, if you are seeing this ,thats because the cloud function was invoked")
