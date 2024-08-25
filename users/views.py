from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm

# Create your views here.

# # Registration View

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", { "form": form })



# Login View
def login_view(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })


# Logout View
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")
    
        
