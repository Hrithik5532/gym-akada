from django.db import models

# Create your models here.


class Banner(models.Model):

    banner = models.ImageField(upload_to='Images/banner-home/')

class Popup(models.Model):    
    popup = models.ImageField(upload_to='Images/popup-home/')
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField( max_length=12,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    # subject = models.CharField(max_length=50,null=True,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.email



class Dietenquiry(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField( max_length=12,null=True,blank=True)
    age = models.IntegerField()
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    reason = models.TextField()
    goal = models.TextField()

    def __str__(self) :
        return self.email
    
class GalleryImages(models.Model):
    img = models.ImageField(upload_to="Gallery/") 


class Testimonials(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True,null=True)
    feedback = models.TextField()
    rating = models.IntegerField(default=0)
