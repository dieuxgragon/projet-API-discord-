from rest_framework import serializers
from models import User, Serveur, Role, Membership, Message, gestionserveur, Demande, Amitier

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nom', 'email']

class ServeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serveur
        fields = ['IDserveur', 'nom', 'Permission']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'nom', 'serveur', 'can_manage_roles', 'can_delete_messages']

class MembershipSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Membership
        fields = ['id', 'user', 'serveur', 'roles', 'joined_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'server', 'author', 'content', 'created_at']

class GestionserveurSerializer(serializers.ModelSerializer):
    class Meta:
        model = gestionserveur
        fields = ['id', 'idutilisateur', 'idserveur']   

class DemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demande
        fields = ['IDdemande', 'libelé', 'statut']

class AmitierSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Amitier
        fields = ['id', 'utilisateur1', 'utilisateur2', 'statut']

