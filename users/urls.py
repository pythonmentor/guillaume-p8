from django.urls import path

from . import views

urlpatterns = [
    # Create user
    path("create_user/", views.create_user, name="create_user"),
    # Modify user
    path("log_in/", views.log_in, name="log_in"),
    # Delete user
    path("delete_user/", views.delete_user, name="delete_user"),
]
