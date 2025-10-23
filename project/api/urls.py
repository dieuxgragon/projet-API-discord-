from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, UserViewSet, FriendshipViewSet,
    ServerViewSet, RoleViewSet, MembershipViewSet, MessageViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"friendships", FriendshipViewSet, basename="friendship")
router.register(r"servers", ServerViewSet, basename="server")
router.register(r"roles", RoleViewSet, basename="role")
router.register(r"memberships", MembershipViewSet, basename="membership")

# messages are nested under server: we'll register message endpoints manually for nested behavior
from rest_framework_nested import routers  # si disponible ; sinon on peut gérer server_pk via URLs

# Simple routes without nested lib:
urlpatterns = [
    path("", include(router.urls)),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # endpoint for messages with server id:
    path("servers/<int:server_pk>/messages/", MessageViewSet.as_view({"get":"list","post":"create"}), name="server-messages"),
    path("servers/<int:server_pk>/messages/<int:pk>/", MessageViewSet.as_view({"get":"retrieve","delete":"destroy"}), name="server-message-detail"),
]
