from rest_framework import viewsets
from ..models import User, Server, Role, Membership, Message, gestionserver, Demande, Amitier
from ..serializer import UserSerializer, ServerSerializer, RoleSerializer, MembershipSerializer, MessageSerializer, GestionserverSerializer, DemandeSerializer, AmitierSerializer      
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    # permission_classes = [IsAuthenticated]

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    # permission_classes = [IsAuthenticated]

class MembershipViewSet(viewsets.ModelViewSet): 
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    # permission_classes = [IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [IsAuthenticated]

class GestionserverViewSet(viewsets.ModelViewSet):
    queryset = gestionserver.objects.all()
    serializer_class = GestionserverSerializer
    # permission_classes = [IsAuthenticated]

class DemandeViewSet(viewsets.ModelViewSet):    
    queryset = Demande.objects.all()
    serializer_class = DemandeSerializer
    # permission_classes = [IsAuthenticated]

class AmitierViewSet(viewsets.ModelViewSet):
    queryset = Amitier.objects.all()
    serializer_class = AmitierSerializer
    # permission_classes = [IsAuthenticated]

