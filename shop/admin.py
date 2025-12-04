from django.contrib import admin
from django.contrib.auth.models import User
from . import models 

admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Client)
admin.site.register(models.Profile)

class ProfileInline(admin.StackedInline):
    model= models.Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username','first_name','last_name','email']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)