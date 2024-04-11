
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view   # for login an logout views

urlpatterns = [
    path("",views.home, name="home"),
    path('register/',views.register, name="register"),
    path('login/',auth_view.LoginView.as_view(template_name='base/login.html'), name="login"),
    path('thanks/',views.thanks, name="thanks"),
]
