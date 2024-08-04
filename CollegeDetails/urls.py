from django.urls import path
from . import views

urlpatterns=[
    path("", view=views.home, name='overview'),
    path("details", view=views.all_colleges, name='all_colleges')
]