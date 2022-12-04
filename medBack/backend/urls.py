from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('blog', BlogForm.as_view(), name='forms'),
    path("register", RegisterUser.as_view(), name='register'),
    path("login", LoginUser.as_view(), name='login'),
    path("shop", shop, name='shop'),
    # path('blog', ),
]