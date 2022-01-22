from django.shortcuts import render, redirect
from .models import AdminDetails, Books
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import random
from django.views.generic.list import ListView
from .serializer import BooksSerializers

# Create your views here.
def OpenLibrary(request):
    return render(request, 'Login.html')    

# login the user here
def UserLogin(request):
    email = request.GET.get('email')
    password = request.GET.get('password')

    login = AdminDetails.objects.filter(email=email, password=password)
    if login:
        messages.success(request, "Login Successfully")
        data = Books.objects.all()
        ser = BooksSerializers(data, many=True)
        context = {
            'book_data': ser.data
        }

        return render(request, 'AdminHome.html', context)
    else:
        messages.error(request, "Failed to login please check email and password")
        return render(request, 'Login.html')    


def Registration(request, tag):
    if tag == 'show':
        return render(request, 'Register.html')
    elif tag == 'register':
        name =  request.GET.get('name')
        email = request.GET.get('email')
        password = request.GET.get('password')
        
        # for security when api get heated
        auth_token = ''.join(random.choice('0123456789ABCDEF') for i in range(52))

      
        if AdminDetails.objects.filter(email=email).exists():
            messages.error(request, "This email account is used by another user let try with new email")
            return render(request,'Login.html')
        else:
            register = AdminDetails(name=name, email=email, password=password, auth_token=auth_token).save()

            if register:
                messages.success(request, "Registration successfully. please login again")
                return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')       

def AddNewBook(request, tag):
    if tag == "show":
        return render(request, 'Register.html')
    elif tag == 'add':
        b_name = request.GET.get('b_name')
        b_publisher = request.GET.get('b_publisher')
        b_type = request.GET.get('b_type')
        auth_token = ''.join(random.choice('0123456789ABCDEF') for i in range(52))

        data = Books(b_name=b_name, b_publisher=b_publisher,b_type=b_type,
              book_token=auth_token).save()

        messages.success(request, "New Book added successfully")
        data = Books.objects.all()
        ser = BooksSerializers(data, many=True)
        context = {
            'book_data': ser.data
        }

        return render(request, 'AdminHome.html', context)     

class AllBookClass(ListView):
    model = Books
    template_name = 'AdminHome.html'
    context_object_name = 'book_data'