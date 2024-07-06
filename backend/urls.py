from django.contrib import admin
from django.urls import path
from backend import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
     path('',views.Login,name='home'),
     path('logout',views.Logout,name='logout'),
     path('dash',views.dashVw,name="dash"),
     path('adduser',views.RegistrationVw,name="adduser"),
     path('viewuser',views.userlist,name="viewuser"),
     path('user/<id>',views.Delete_user,name="user"),
     path('Delete_customer/<id>',views.Delete_customer,name="Delete_customer"),
     path('viewcustomer',views.cus_list,name="viewcustomer"),
     path('addcustomer',views.addcustomer,name="addcustomer"),
     path('updates_cus_list/<id>',views.updates_cus_list,name='updates_cus_list'),
     
]   