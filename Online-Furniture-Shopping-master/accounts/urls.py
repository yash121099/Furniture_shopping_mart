from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('otp/', views.otp, name="otp"),
    path('validateotp/', views.validateotp, name="validateotp"),
    path('resend/', views.resend, name="resend"),
    path('logout/', views.logout_req, name="logout")
]
