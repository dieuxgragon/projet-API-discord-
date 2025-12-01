# views.py
from django.http import JsonResponse
from .models import User, Server, Role, Membership, Message, gestionserver, Demande, Friendship
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .serializer import UserSerializer, ServerSerializer, RoleSerializer, MembershipSerializer, MessageSerializer, GestionserverSerializer, DemandeSerializer, FriendshipSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
def api_server_list(request):  
    servers = Server.objects.all()
    serializer = ServerSerializer(servers, many=True)
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
def api_gestionserver_list(request):  
    gestionservers = gestionserver.objects.all()
    serializer = GestionserverSerializer(gestionservers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_demande_list(request):  
    demandes = Demande.objects.all()
    serializer = DemandeSerializer(demandes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_amitier_list(request):  
    friendship = Friendship.objects.all()
    serializer = FriendshipSerializer(friendship, many=True)
    return Response(serializer.data)
