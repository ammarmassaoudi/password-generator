from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),

]
