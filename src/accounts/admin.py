from django.contrib import admin

from accounts.models import CustomUser, Profile

admin.site.register([CustomUser, Profile])