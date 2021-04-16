from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login, get_user_model
User = get_user_model()

# Create your views here.

# def index(request):
#     request.session.set_test_cookie()
#     return HttpResponse("<h1>Welcome to home </h1>")


# def check_view(request):
#     if (request.session.test_cookie_worked()):
#         print("cookies are working properly")
#         request.session.delete_test_cookie()
#         return HttpResponse("<h1>Checking Page..</h1>")


def home(request):
    return render(request, 'home.html')


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        response = render(request, 'main.html')
        return response


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('data')

    return render(request, 'login.html')


def logout_view(request):

    logout(request)

    return redirect('login')
