
from django.urls import path
# from knox import views as knox_views
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
#from users import views

urlpatterns = [
    path('hello/',views.HelloView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('user/', views.get_user),
    path('login/', views.login),
    path('register/', views.register),
    # path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]