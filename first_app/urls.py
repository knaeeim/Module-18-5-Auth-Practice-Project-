from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="home"),
    path('signup/', signinPage, name="signup"),
    path('login/', loginpage, name="login"),
    path('profile/', profile, name="profile"),
    path('logout/', logoutpage, name="logout"),
    path('change_password/', change_password, name="change_password"),
    path('reset_password/', reset_password, name="reset_password"),
    path('update_profile/', update_profile, name="update_profile"),
]
