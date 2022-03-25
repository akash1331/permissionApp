from django.db import models

# Create your models here.

class permission(models.Model):
    date = models.DateField(auto_now_add=True)
    from_time = models.TimeField(auto_now_add=False)
    out_date = models.TimeField(auto_now_add=False)
    reason = models.TextField()
    attachment = models.FileField(upload_to=None,null = True,blank=True)
    granted = models.BooleanField(default = False)

