from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(UserAccount)
# # Register your models here.

@admin.register(UserAccount)
class postadmin(admin.ModelAdmin):
    
    list_display = ['id','roll_no','email','first_name','last_name','branch']
    class Meta:
        model = UserAccount