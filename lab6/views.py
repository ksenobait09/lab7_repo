from django.shortcuts import render
from django.views import View
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from lab6.models import Book
from lab6.forms import *


# Create your views here.
def main(request):
    books = Book.objects.all()

    return render(request, 'main.html', {'books': books} )

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form':form})

def signin(request):
    redirect = '/success'
    if request.method == "POST":
        username =request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            auth.login(request,user)
            return HttpResponseRedirect(redirect)
        else:
            return HttpResponseRedirect('/')
    return render (request, 'signin.html',)

@login_required()
def success(request):
    if request.user.is_authenticated():
        return render(request, 'success.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def booksModel(request):
    return render(request, 'formmodel.html', {'form': ArticleForm()})