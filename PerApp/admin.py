from django.contrib import admin

from PerApp.models import *

# Register your models here.

class permissionAdminSite(admin.ModelAdmin):
    list_display = ('date','from_time','out_date','reason','attachment','granted')

class studentAdminSite(admin.ModelAdmin):
    list_display = ('roll_number','first_name','last_name','branch','dp')



admin.site.register(permission,permissionAdminSite)
# admin.site.register(student,studentAdminSite)

admin.site.site_header = 'BVRIT App admin'