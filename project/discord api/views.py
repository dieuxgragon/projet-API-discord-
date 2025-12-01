# views.py
from django.http import JsonResponse
from .models import User, Serveur, Role, Membership, Message, gestionserveur, Demande, Amitier
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .serializer import UserSerializer, ServeurSerializer, RoleSerializer, MembershipSerializer, MessageSerializer, GestionserveurSerializer, DemandeSerializer, AmitierSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@login_required
def dashboard(request):
    return HttpResponse("Welcome to your dashboard!")

@api_view(['GET'])
def user_list(request):
    users = User.objects.all().values('name', 'datedenaissance', 'pseudo')
    return JsonResponse(list(users), safe=False)

@api_view(['GET'])
def api_serveur_list(request):  
    serveurs = Serveur.objects.all()
    serializer = ServeurSerializer(serveurs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_role_list(request): 
    roles = Role.objects.all()
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_membership_list(request):  
    memberships = Membership.objects.all()
    serializer = MembershipSerializer(memberships, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_message_list(request):  
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_gestionserveur_list(request):  
    gestionserveurs = gestionserveur.objects.all()
    serializer = GestionserveurSerializer(gestionserveurs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_demande_list(request):  
    demandes = Demande.objects.all()
    serializer = DemandeSerializer(demandes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_amitier_list(request):  
    amities = Amitier.objects.all()
    serializer = AmitierSerializer(amities, many=True)
    return Response(serializer.data)

