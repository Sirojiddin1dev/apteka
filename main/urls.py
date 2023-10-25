from django.urls import *
from .views import *

urlpatterns = [
    path('index', index_view, name='index_url'),
    path('', signup_view, name="signup_url"),
    path('login/', signin_view, name="login_url"),
    path('shop/', shop_view, name='shop_url'),
    path('about/', about_view, name='about_url'),
    path('contact/', contact_view, name='contact_url'),
    path('my-profile/', my_profile_view, name='my_profile_url'),
]
