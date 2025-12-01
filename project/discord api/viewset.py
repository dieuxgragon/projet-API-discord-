from rest_framework import viewsets
from .models import User, Serveur, Role, Membership, Message, gestionserveur, Demande, Amitier
from .serializer import UserSerializer, ServeurSerializer, RoleSerializer, MembershipSerializer, MessageSerializer, GestionserveurSerializer, DemandeSerializer, AmitierSerializer      
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

class ServeurViewSet(viewsets.ModelViewSet):
    queryset = Serveur.objects.all()
    serializer_class = ServeurSerializer
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

class GestionserveurViewSet(viewsets.ModelViewSet):
    queryset = gestionserveur.objects.all()
    serializer_class = GestionserveurSerializer
    # permission_classes = [IsAuthenticated]

class DemandeViewSet(viewsets.ModelViewSet):    
    queryset = Demande.objects.all()
    serializer_class = DemandeSerializer
    # permission_classes = [IsAuthenticated]

class AmitierViewSet(viewsets.ModelViewSet):
    queryset = Amitier.objects.all()
    serializer_class = AmitierSerializer
    # permission_classes = [IsAuthenticated]

