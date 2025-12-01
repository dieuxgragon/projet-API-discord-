from django.contrib import admin
from .models import User, Amitier, Server, Role, Membership, Message

admin.site.register(User)
admin.site.register(Amitier)
admin.site.register(Server)
admin.site.register(Role)
admin.site.register(Membership)
admin.site.register(Message)
