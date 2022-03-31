from datetime import date
from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.files import ImageField
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
from twilio.rest import Client
from django.utils.text import slugify
import random, string
from django.db.models.signals import pre_save


# Create your models here.
# class student(models.Model):
#     roll_number=models.CharField(max_length=10,unique=True)
#     first_name= models.TextField()
#     last_name=models.TextField()
#     branch = models.TextField()
#     dp = models.ImageField(upload_to='profileDp',null = True)


#     def __str__(self):
#         return self.roll_number


class permission(models.Model):
    # student_roll =models.ForeignKey(student,on_delete=SET_NULL,null=True)
    roll_number=models.CharField(max_length=10,null=True)
    date = models.DateField(auto_now_add=True)
    from_time = models.TimeField(auto_now_add=False)
    out_date = models.TimeField(auto_now_add=False)
    reason = models.TextField()
    attachment = models.FileField(upload_to='attachments',null = True,blank=True)
    granted = models.BooleanField(default = False)
    qr_code = models.ImageField(upload_to='qr_code',blank=True)
    slug = models.SlugField(blank=True,null=True)


    def __str__(self):
        return self.reason


    def slug_generator(sender,instance,args,*kwargs):
        if not instance.slug:
            instance.slug = permission.unique_slug_generator(instance)
            pre_save.connect(permission.slug_generator,sender=permission)

    def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def unique_slug_generator(instance, new_slug=None):
        if new_slug is not None:
            slug = new_slug
        else:
            slug = slugify(instance.roll_number,instance.granted)

        Klass = instance._class_
        qs_exists = Klass.objects.filter(slug=slug).exists()
        if qs_exists:
            new_slug = "{slug}-{randstr}".format(
                slug=slug,
                randstr=permission.random_string_generator(size=4)
            )
            return permission.unique_slug_generator(instance, new_slug=new_slug)
        return slug

    def save(self,*args,**kwargs):
        qr_image = qrcode.make(self.slug)
        qr_offset = Image.new('RGB',(310,310),'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.roll_number}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream,'PNG')
        self.qr_code.save(files_name,File(stream),save=False)
        qr_offset.close()
        super().save(*args,**kwargs)

        if self.granted == True:
            account_sid = 'AC5077b647d114a5139a086ca96309cb0b'
            auth_token =  '872debd26f5f68f66413c2c1d82961a0'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'Your child has been granted permission from college at {self.from_time} with reason {self.reason}',
                from_= '+19898000748',
                to='+919392964690'
                )

            print(message.sid)
            return super().save(*args,**kwargs)

