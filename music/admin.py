from django.contrib import admin

# Register your models here.
# Here I have registered manually

from .models import Album,Song
admin.site.register(Album)
admin.site.register(Song)


