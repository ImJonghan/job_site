
from django.urls import path

from . import views

app_name='lion'

urlpatterns = [    
    path("", views.JobLV.as_view(), name="index"),
    path("detail/<int:pk>/", views.JobDV.as_view(), name="detail"),
    path("upload/", views.image_upload_view, name='upload'),
]