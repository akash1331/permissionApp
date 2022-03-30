from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import datetime
import random
from PerApp.models import *

def unique_usernumber(instance, new_id=None):
    ct = datetime.datetime.now().date()
    number = 1
    if new_id is not None:
        id = new_id
    else:
        id = 'f' + str(ct) +str(number)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(user_id=id).exists()
    if qs_exists:
        new_id = "f{date}{idgen}{rand}".format(
            
            date=ct,
            idgen = number+1,
            rand = random.randrange(0, 100000),
        )
        return unique_usernumber(instance, new_id=new_id)
    
    return id


class UserAccountManager(BaseUserManager):

    def create_superuser (self, email,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
             raise ValueError(
                 "Superuser must be assigned to is_staff=True.")
        if other_fields.get('is_superuser') is not True:
             raise ValueError(
                 'Superuser must be assigned to is superuser=True.')
        return self.create_user(email,password, **other_fields)



    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.is_superuser = True
        user.save()

        return user
  
ACCOUNT_TYPEE = (
    ("STUDENT", "student"),
    ("SECURITY", "security"),
    ("ADMIN", "admin"),
    ("SUPERADMIN", "superadmin"),

)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=255,default="S")
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roll_no = models.CharField(max_length = 10,null=True)
    parent_phone = models.IntegerField(blank=True,null=True)
    student_phone= models.IntegerField(blank=True,null=True)
    branch = models.CharField(max_length=8,null=True)
    hostler = models.BooleanField(default=False)
    grantedby = models.CharField(max_length=50,blank=True)
    dp = models.ImageField(upload_to='profileDp',null = True)
    type_of_account = models.CharField(
        max_length = 20,
        choices = ACCOUNT_TYPEE,
        default = 'STUDENT'
        )
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name +" " + self.last_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email

def user_number_generator(sender,instance,*args,**kwargs):
    if  instance.user_id:
        instance.user_id = unique_usernumber(instance)
pre_save.connect(user_number_generator,sender=UserAccount)
