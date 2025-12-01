from rest_framework import serializers
from .models import User, Server, Role, Membership, Message, gestionserver, Demande, Friendship

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nom', 'email']

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['IDserver', 'nom', 'Permission']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'nom', 'server', 'can_manage_roles', 'can_delete_messages']

class MembershipSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Membership
        fields = ['id', 'user', 'server', 'roles', 'joined_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'server', 'author', 'content', 'created_at']

class GestionserverSerializer(serializers.ModelSerializer):
    class Meta:
        model = gestionserver
        fields = ['id', 'idutilisateur', 'idserver']   

class DemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demande
        fields = ['IDdemande', 'libelé', 'statut']

class FriendshipSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Friendship
        fields = ['id', 'utilisateur1', 'utilisateur2', 'statut']

