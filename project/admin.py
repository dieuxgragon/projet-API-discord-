from django.contrib import admin
from .models import User, Friendship, Serveur, Role, Membership, Message

admin.site.register(User)
admin.site.register(Friendship)
admin.site.register(Serveur)
admin.site.register(Role)
admin.site.register(Membership)
admin.site.register(Message)
