from django.urls import path
from .views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home),


]
urlpatterns += staticfiles_urlpatterns()
