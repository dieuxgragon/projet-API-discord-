from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    path("dashboard/", views.dashboard, name="dashboard"),
    
    path("users/simple/", views.user_list, name="user_list_simple"),

    path("api/users/", views.api_user_list, name="api_user_list"),
    path("api/servers/", views.api_server_list, name="api_server_list"),
    path("api/roles/", views.api_role_list, name="api_role_list"),
    path("api/memberships/", views.api_membership_list, name="api_membership_list"),
    path("api/messages/", views.api_message_list, name="api_message_list"),
    path("api/gestionservers/", views.api_gestionserver_list, name="api_gestionserver_list"),
    path("api/demandes/", views.api_demande_list, name="api_demande_list"),
    path("api/amitier/", views.api_amitier_list, name="api_amitier_list"),
]