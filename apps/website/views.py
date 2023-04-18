from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings      # added Makers Group

def home(request):
	return render(request, 'home.html', {})

def contact(request):
# for dough in contact we do a POST request
# if somebody one does POST a Page
	if request.method == "POST":
		#python doesn't like hyphens, so repl with underscore
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send an email (using send_mail function)
		send_mail(
			#geen effect still error fail_silently '
			                # message_name, #title
			#message_name,  # subject 'message from ' +
			#'hoi ' + message_name + ' u hebt' + message,   # subject werkt niet new line error
			# misschien de message tekst op een andere meer uitbreiden.. Get in Touch met ....

			'hoi ' + message_name + ' u hebt ons een bericht',   # subject
			message,                         # message
			'settings.EMAIL_HOST_USER',      # Makers G - sender, if not available 
			                                 #     considered the default or configured
			[message_email],                  # from email
			#['wads.vanvelthoven@gmail.com',], # to email 2e email put komma and 2e adres 
											 # email of emailadres?
			fail_silently=False
			)
		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})	

def pricing(request):
	return render(request, 'pricing.html', {})	

def service(request):
	return render(request, 'service.html', {})	

def appointment(request):
# for dough in contact we do a POST request
# if somebody one does POST a Page
	if request.method == "POST":
		your_name	  = request.POST['your-name']
		your_phone	  = request.POST['your-phone']
		your_email	  = request.POST['your-email']
		your_address  = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date	  = request.POST['your-date']
		your_message  = request.POST['your-message']

		
		#python doesn't like hyphens, so repl with underscore
		
		#send an email (using send_mail function)
		appointment = 'Name: ' + your_name + ' Phone: ' + your_phone + ' Email: ' + your_email + ' Address: ' + your_address + ' Schedule: ' + your_schedule + ' Day: ' + your_date + ' Message: ' + your_message
		#format uitzoeken
		send_mail(
			'Appointment request',           # subject
			appointment,                     # message
			'settings.EMAIL_HOST_USER',      # Makers G - sender, if not available 
			                                 #     considered the default or configured
			[your_email],                    # from email
			#['wads.vanvelthoven@gmail.com',], # to email 2e email put komma and 2e adres 
											 # email of emailadres?
			fail_silently=False
			)
		
		return render(request, 'appointment.html', {
			'your_name':	  your_name,
			'your_phone':	  your_phone,
			'your_email':	  your_email,
			'your_address':   your_address,
			'your_schedule':  your_schedule,
			'your_date':	  your_date,
			'your_message':   your_message
			 })
	else:
		return render(request, 'home.html', {}) #we will redirect to the home page