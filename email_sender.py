import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Luciana Miyuki'
email['to'] = 'lucianamiyukiyonamine@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('lucianamiyukiyonamine@gmail.com', 'miyuki1310')
	smtp.send_message(email)
	print('All good boss!')	