from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.unregister(Group)
