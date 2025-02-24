from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("send-verification-email/", views.send_verification_email, name="send_verification_email"),
    path("verify-email/<str:token>/", views.verify_email, name="verify_email"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path('shared-posts/', views.shared_posts, name='shared_posts'),
]
