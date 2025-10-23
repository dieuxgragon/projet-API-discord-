from rest_framework import serializers
from .models import User, Friendship, Server, Role, Membership, Message
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"]
        )
        return user

class FriendshipSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)
    to_user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Friendship
        fields = ["id", "from_user", "to_user", "to_user_id", "accepted", "created_at"]
        read_only_fields = ("accepted", "created_at")

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "name", "server", "can_manage_roles", "can_delete_messages"]
        read_only_fields = ("server",)

class ServerSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = Server
        fields = ["id", "name", "description", "owner", "created_at", "roles"]

class MembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    server = ServerSerializer(read_only=True)
    server_id = serializers.IntegerField(write_only=True)
    role_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)

    class Meta:
        model = Membership
        fields = ["id", "user", "server", "server_id", "role_ids", "joined_at"]

    def create(self, validated_data):
        user = self.context["request"].user
        server_id = validated_data.pop("server_id")
        role_ids = validated_data.pop("role_ids", [])
        server = Server.objects.get(pk=server_id)
        membership, created = Membership.objects.get_or_create(user=user, server=server)
        if role_ids:
            roles = Role.objects.filter(id__in=role_ids, server=server)
            membership.roles.set(roles)
        membership.save()
        return membership

class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    server = serializers.PrimaryKeyRelatedField(queryset=Server.objects.all())

    class Meta:
        model = Message
        fields = ["id", "server", "author", "content", "created_at"]
        read_only_fields = ("author", "created_at")

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
