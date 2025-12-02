from django.urls import path
from . import views
from .views import online_users

app_name = "presence"

urlpatterns = [
    path("session-expired/", views.session_expired, name="session_expired"),
    path("online/", online_users, name="online-users"),
]
