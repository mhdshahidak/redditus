from email.policy import default
from enum import unique
from msilib.schema import Class
from trace import Trace
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.forms import IntegerField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('User must have a email')
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user:
            return user
    def create_superuser(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('User must have a email')
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff   = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    shop_name = models.CharField(max_length=60,null=True)
    email=models.EmailField(unique=True)
    address = models.CharField(max_length=500,null=True)
    place = models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD='email'



# Client

class Client(models.Model):
    client_name = models.CharField(max_length=50,null=True)
    phone_no =  PhoneNumberField(unique=True)
    address = models.CharField(max_length=500,null=True)


# Catagory

class Catagory(models.Model):
    cat_name = models.CharField(max_length=40,null=True)


# stock

class Stock(models.Model):
    item_name = models.CharField(max_length=40)
    item_catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0)
    buying_price = models.FloatField(null=True)
    rental_price = models.FloatField(null=True)
    damage_price = models.FloatField(null=True)
    missing_price = models.FloatField(null=True)


# billing 

class Billing(models.Model):
    status_choices = (('not returned','not returned'),('returned','returned'),('other','other'))
    billing_no = models.CharField(max_length=50,unique=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=True)
    billing_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=20,default="not returned",choices=status_choices)

    

#billing product

class BillingProducts(models.Model):
    status_choices = (('not returned','not returned'),('returned','returned'),('other','other'))
    billing = models.ForeignKey(Billing,on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Stock,on_delete=models.CASCADE,null=True)
    qty = models.IntegerField(default=0)
    billing_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default="not returned",choices=status_choices)



class expencecatagory(models.Model):
    catagory = models.CharField(max_length=50)


class expence(models.Model):
    date = models.DateTimeField(null=True)
    catagory = models.ForeignKey(expencecatagory,on_delete=models.CASCADE,null=True)
    note = models.CharField(max_length=500,null=True)
    amount = models.FloatField()


class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    acc_holder_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=50)
    acc_number = models.BigIntegerField()
    branch = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    amount = models.FloatField(default=0)


class IncomeCategory(models.Model):
    category = models.CharField(max_length=100)


class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(null=True)
    amount = models.FloatField()
    note = models.CharField(max_length=500,null=True)


# Return Items 

class returnitems(models.Model):
    billing_no = models.ForeignKey(Billing, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(BillingProducts, on_delete=models.CASCADE, null=True)
    return_date = models.DateField(null=True)
    returned_qty = models.IntegerField(default=0)
    damage_qty  = models.IntegerField(default=0)
    missing_qty = models.IntegerField(default=0)
    total_amount = models.FloatField(null=True)


class invoicepaymethode(models.Model):
    bill = models.ForeignKey(Billing, on_delete=models.CASCADE, null=True)
    pay_type = models.CharField(max_length=30,null=True)
    amount = models.FloatField()
    date = models.DateField(null=True)
    