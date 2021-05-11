from django.contrib import admin

# Register your models here.
from .models import News, SportNews, RegistrationData


admin.site.register(News)
admin.site.register(SportNews)
admin.site.register(RegistrationData)