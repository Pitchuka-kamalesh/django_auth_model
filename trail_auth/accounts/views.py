from django.shortcuts import render,redirect
from .forms import RegisterForm


# Create your views here.

def signup_page(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    data = {'form':form}
    return render(request, 'signup.html',context=data)