from django.shortcuts import render, HttpResponse
from .models import Home, Portfolio,Contact
from django.contrib import messages

# Create your views here.
def home(request):
    homes = Home.objects.all()
    projects = Portfolio.objects.all()
    context = {
        'homes':homes,
        'projects':projects,
        }
    return render(request,'home.html',context)
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if len(name)<3 or len(email)<11 or len(phone)<6 or len(message)<4:
            messages.error(request,"Please fill the form correctly")

        else:
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request,"Your messages is been sent!")
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
