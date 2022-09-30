from django.contrib import admin

from core.models import Profile, CustomUser

admin.site.register([CustomUser, Profile])
