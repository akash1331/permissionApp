from django.contrib import admin

from PerApp.models import *

# Register your models here.

class permissionAdminSite(admin.ModelAdmin):
    list_display = ('roll_number','student_roll','date','from_time','out_date','reason','attachment','granted')


admin.site.register(permission,permissionAdminSite)
admin.site.site_header = 'BVRIT App admin'