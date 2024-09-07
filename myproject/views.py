
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
import urllib.parse
from .forms import WhatsAppForm
from posts.models import Post

def home(request):
    posts = Post.objects.all().order_by('-date')
    if request.user.is_authenticated:
        welcome_message = f"Welcome to the my awesome blog, Dear {request.user.username} ❤️❤️❤️"
    else:
        welcome_message = "Welcome to the awesome blog dear visitor ❤️❤️❤️"

    context = {'posts': posts, 'welcome_message': welcome_message}
    return render(request, 'home.html', context)






def about(request):
    if request.method == 'POST':
        form = WhatsAppForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            # Encoded message for my WhatsApp
            whatsapp_url = encode_whatsapp_message(name, last_name, email, phone_number, message)
            
            # Send the form to my email
            email_subject = "Hi, a form has been submitted to your whatsapp account, below also is the form"
            email_body = (
                f"Hello,\n\n"
                f"You have received a new WhatsApp form submission:\n\n"
                f"*Name:* {name}\n"
                f"*Last Name:* {last_name}\n"
                f"*Email:* {email}\n"
                f"*Phone Number:* {phone_number}\n\n"
                f"*Message:* {message}\n"
            )
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                ['abdulsomad005@gmail.com'],  
                fail_silently=False,
            )
            
            # Redirecting to WhatsApp
            return redirect(whatsapp_url)
    else:
        form = WhatsAppForm()

    return render(request, 'about.html', {'form': form})

def encode_whatsapp_message(name, last_name, email, phone_number, message):
    
    message_body = (
        f"Hello Roslaan,\n\n"
        f"*Name:* {name}\n"
        f"*Last Name:* {last_name}\n"
        f"*Email:* {email}\n"
        f"*Phone Number:* {phone_number}\n\n"
        f"*Message:* {message}\n"
    )
    
    # URL-encoding the message gto accept different character 
    encoded_message = urllib.parse.quote(message_body)
    
    # My WhatsApp number in the international format
    whatsapp_number = "+2347048839991"
    
    # Constructing the WhatsApp URL
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"
    
    return whatsapp_url
