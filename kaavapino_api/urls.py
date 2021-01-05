from django.urls import path, re_path
from rest_framework.versioning import URLPathVersioning
from kaavapino_api import views

urlpatterns = [
    path('heartbeat',
         views.heartbeat.API.as_view(),
         name='heartbeat'),
]
