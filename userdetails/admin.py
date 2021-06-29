from django.contrib import admin
from .models import City, District, Country, State, UserDetails
# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
admin.site.register(UserDetails)
admin.site.register(State)