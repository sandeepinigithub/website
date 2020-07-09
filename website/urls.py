from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url('music/',include('music.urls')),
]
