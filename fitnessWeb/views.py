from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    if  request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        number =request.POST.get('number')
        age=request.POST.get('age')
        height =request.POST.get('height')
        weight =request.POST.get('weight')
        reason =request.POST.get('reason')
        goal =request.POST.get('goal')


        if Dietenquiry.objects.filter(email=email).exists():
            messages.error(request,' Email Id Already in use.')
            return redirect('home')
        
        contact =Dietenquiry.objects.create(email=email,name=name,phone=number,age=age,height=height,weight=weight,reason=reason,goal=goal)
        contact.save()
        messages.success(request,"We will Reach You Soon.. !!")
    
        return redirect('home')
    banner =Banner.objects.first()
    gallery_img = GalleryImages.objects.all()[0:6]

    popup = Popup.objects.first()
    return render(request,'html/index.html',{'title':'Home','gallery_img':gallery_img,'banner':banner,'popup':popup})


def about(request):
    testimonials =Testimonials.objects.all()
    print(testimonials)
    return render(request,'html/about-us.html',{'title':'About Us','testimonials':testimonials})


def gallery(request):
    gallery_img = GalleryImages.objects.order_by('-id').all()
    img_count = gallery_img.count()
    print(img_count)
    return render(request,'html/gallery.html',{'title':'Gallery',"gallery_img":gallery_img,'img_count':img_count})
def Bmi(request):
    return render(request,'html/bmi-calculator.html',{'title':'BMI Calculator'})

def contact(request):
    if  request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        number =request.POST.get('number')
        message =request.POST.get('message',None)

        contact =Contact.objects.create(email=email,name=name,phone=number,message=message)
        contact.save()
        messages.success(request,"Reach You Soon !!")
        return redirect('contact')
    
    return render(request,'html/contact.html',{'title':"Contact Us"})
