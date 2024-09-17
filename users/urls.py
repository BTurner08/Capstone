from django.urls import path
from .views import UserLoginView, UserRegisterView, contact, log_user_out, EditProfile

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", log_user_out, name="logout"),
    path("contact/", contact, name="contact"),
    path("edit_profile/", EditProfile.as_view(), name="edit_profile"),
]