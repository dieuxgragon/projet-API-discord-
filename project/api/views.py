import serializers
from rest_framework import viewsets, status, generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from . import models
from .models import User, Friendship, Server, Role, Membership, Message
from .serializers import (
    UserSerializer, RegisterSerializer, FriendshipSerializer,
    ServerSerializer, RoleSerializer, MembershipSerializer, MessageSerializer
)
from .permissions import IsServerMember, IsServerOwnerOrRoleCanManage

# Registration & user
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Friendship endpoints
class FriendshipViewSet(viewsets.ModelViewSet):
    serializer_class = FriendshipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(models.Q(from_user=user) | models.Q(to_user=user))

    def perform_create(self, serializer):
        to_user_id = serializer.validated_data.get("to_user_id")
        to_user = get_object_or_404(User, pk=to_user_id)
        if to_user == self.request.user:
            raise serializers.ValidationError("You cannot friend yourself.")
        # avoid duplicate
        obj, created = Friendship.objects.get_or_create(from_user=self.request.user, to_user=to_user)
        if not created:
            raise serializers.ValidationError("Request already sent.")
        return obj

    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        fr = self.get_object()
        if fr.to_user != request.user:
            return Response({"detail": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)
        fr.accept()
        return Response(self.get_serializer(fr).data)

# Server endpoints
class ServerViewSet(viewsets.ModelViewSet):
    serializer_class = ServerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # list all servers (or filter to servers where user is member if you prefer)
        return Server.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def join(self, request, pk=None):
        server = self.get_object()
        membership, created = Membership.objects.get_or_create(user=request.user, server=server)
        if created:
            return Response(MembershipSerializer(membership, context={"request": request}).data, status=status.HTTP_201_CREATED)
        return Response(MembershipSerializer(membership, context={"request": request}).data)

    @action(detail=True, methods=["post"], permission_classes=[IsServerOwnerOrRoleCanManage])
    def create_role(self, request, pk=None):
        server = self.get_object()
        data = request.data.copy()
        data["server"] = server.id
        serializer = RoleSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(server=server)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Roles viewset for updating / deleting roles (permissioned)
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsServerOwnerOrRoleCanManage]

# Memberships
class MembershipViewSet(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # show memberships of current user or server members if server_pk provided
        user = self.request.user
        server_pk = self.kwargs.get("server_pk")
        if server_pk:
            return Membership.objects.filter(server_id=server_pk)
        return Membership.objects.filter(user=user)

# Messages
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related("author", "server").all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsServerMember]

    def get_queryset(self):
        server_pk = self.kwargs.get("server_pk")
        if server_pk:
            return self.queryset.filter(server_id=server_pk)
        return self.queryset.none()  # avoid listing all messages globally

    def perform_create(self, serializer):
        server = serializer.validated_data["server"]
        # check membership explicitly
        if not Membership.objects.filter(user=self.request.user, server=server).exists():
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You must be a member of the server to post messages.")
        serializer.save(author=self.request.user)
