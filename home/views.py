from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#this is my password: Akshay###$$$

def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, "index.html")
    else:
        return redirect("/login")
    
    

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            return render(request, "login.html")
    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("/login")
