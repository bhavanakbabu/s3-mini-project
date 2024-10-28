from django.contrib import admin
from .models import userreg, bin, driver, regcomp, drivstatus, Notification

# Register your models here.

# Customize the userreg admin panel
class UserRegAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')  # Fields displayed in the list
    search_fields = ('username', 'email')          # Fields to search by

# Customize the bin admin panel
class BinAdmin(admin.ModelAdmin):
    list_display = ('area', 'landmark', 'dmail', 'period')
    search_fields = ('area', 'landmark', 'dmail')

# Customize the driver admin panel
class DriverAdmin(admin.ModelAdmin):
    list_display = ('dname', 'demail', 'darea')
    search_fields = ('dname', 'demail')

# Customize the registered complaints (regcomp) admin panel
class RegCompAdmin(admin.ModelAdmin):
    list_display = ('rarea', 'remail', 'status')
    list_filter = ('status',)  # Adds a filter sidebar for the status field
    search_fields = ('rarea', 'remail')

# Customize the driver status (drivstatus) admin panel
class DrivStatusAdmin(admin.ModelAdmin):
    list_display = ('drivername', 'area', 'status')
    list_filter = ('status',)  # Adds a filter sidebar for the status field
    search_fields = ('drivername', 'area')

# Customize the notification admin panel
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')  # Adds a filter sidebar for these fields
    search_fields = ('user__username', 'message')  # Allows searching by username and message content

# Register the models and their admin classes
admin.site.register(userreg, UserRegAdmin)
admin.site.register(bin, BinAdmin)
admin.site.register(driver, DriverAdmin)
admin.site.register(regcomp, RegCompAdmin)
admin.site.register(drivstatus, DrivStatusAdmin)
admin.site.register(Notification, NotificationAdmin)
