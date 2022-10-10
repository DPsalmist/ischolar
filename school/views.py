from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, PayFeesForm
from django.core.mail import send_mail, EmailMessage

# Create your views here.
def index(request):
	return render(request,'index.html')
	
def about(request):
	return render(request,'about.html')

def admission(request):
	return render(request,'admission.html')

def news(request):
	return render(request,'news.html')

def gallery(request):
	return render(request,'gallery.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
        	contact_name = form.cleaned_data['name']
        	contact_email = form.cleaned_data['email']
        	subject = form.cleaned_data['subject']
        	contact_message = f"{contact_name} has sent you a new message ..."
        	email_msg = EmailMessage(
        		subject=subject, body=contact_message, 
        		from_email='dpsalmist546@gmail.com',  #your Zoho domain name(i createdan external email)
         		to=['dpsalmist546@gmail.com'],
        		headers={'Reply-To': contact_email})
        	email_msg.send()
        	messages.success (request, f'Thank you for contacting us!.')
        	return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def payfees(request):
	if request.method == 'POST':
		form = PayFeesForm(request.POST)
		if form.is_valid():
			return HttpResponse ('Thanks for the payment')
	else:
		form = PayFeesForm()

	return render(request,'payfees.html', {'form': form})

