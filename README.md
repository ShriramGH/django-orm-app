# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![Screenshot 2023-05-30 233346](https://github.com/ShriramGH/django-orm-app/assets/117991122/2294c1d8-6b1b-4ab0-9416-df9d0532e5ac)

## DESIGN STEPS

### STEP 1:
Create a new Django project using "django-admin startproject",get into the project terminal and use "python3 manage.py startapp" command.

### STEP 2:
Define a model for the BankAccountmembership in the models.py.Allow host access and add the app name under installed apps in settings.py

### STEP 3:
Register the models with the Django admin site. In admin.py under app folder,register the models with Django admin site.

### STEP 4:
Run the python manage.py makemigrations and python manage.py migrate commands to create the necessary database tables for the BankAccountmembership model.Run the Server using "python3 manage.py runserver 0:80" command.

## PROGRAM
```
#IN models.py:-

from django.db import models
from django.contrib import admin
#Create your model here.
class BankAccountMember(models.Model):
    account_number = models.CharField(max_length=16,primary_key=True)
    name =models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.IntegerField()

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number','name','age','email','phone_number')

#IN admin.py:-

from django.contrib import admin
from .models import BankAccountMember,BankAccountAdmin

admin.site.register(BankAccountMember,BankAccountAdmin)
```

## OUTPUT

![Screenshot 2023-05-30 233346](https://github.com/ShriramGH/django-orm-app/assets/117991122/3445c82f-67cc-41aa-9f70-f27daf6115bc)



## RESULT

Successfully developed a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).
