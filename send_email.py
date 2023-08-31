import smtplib,ssl
def send_email():
    host = 'smpt.gmail.com'
    port = 465

    username = 'akbulutsimge53@gmail.com'
    password = 'zqlkotebqkvjeccg'

    reciever = 'akbulutsimge53@gmail.com'
    context = ssl.create_default_context()

    message = '''
    Hi!
    How are you?
    Bye!!
    '''

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(username,password)
        server.sendmail(username,reciever, message)
send_email()