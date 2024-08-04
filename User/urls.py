from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.get_users, name='get_users'),
    path('add_users', view=views.add_users, name="add_users"),
    path('<int:id>', view=views.user_detail, name="user_detail")
]