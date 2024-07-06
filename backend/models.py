from django.db import models

# Create your models here.
class Registration_DB(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=True) 
#-------add customer----------#   
class customer_DB(models.Model):
    name = models.CharField(max_length=100,default="")
    mobile = models.PositiveBigIntegerField()
    dob = models.TextField()
    addr = models.TextField()
    service_type = models.CharField(max_length=100,default="")
    curr_date = models.TextField()
    image = models.ImageField(upload_to="media/cus_img",default=" ")
    application_no = models.PositiveBigIntegerField()
    user = models.CharField(max_length=100,default="")
    remark = models.TextField()
    
    status = models.BooleanField(default=True)  
class Test(models.Model):
    image=models.ImageField(upload_to='test')

# Create your models here.
