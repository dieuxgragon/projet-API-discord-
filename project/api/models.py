from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    # tu peux ajouter des champs si besoin (avatar, bio, ...)
    pass

class Friendship(models.Model):
    # friendship request model
    from_user = models.ForeignKey(User, related_name="friend_requests_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="friend_requests_received", on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("from_user", "to_user")

    def accept(self):
        self.accepted = True
        self.save()

class Server(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name="owned_servers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    server = models.ForeignKey(Server, related_name="roles", on_delete=models.CASCADE)
    can_manage_roles = models.BooleanField(default=False)
    can_delete_messages = models.BooleanField(default=False)

    class Meta:
        unique_together = ("name", "server")

    def __str__(self):
        return f"{self.name} @ {self.server.name}"

class Membership(models.Model):
    user = models.ForeignKey(User, related_name="memberships", on_delete=models.CASCADE)
    server = models.ForeignKey(Server, related_name="members", on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role, related_name="members", blank=True)
    joined_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("user", "server")

    def __str__(self):
        return f"{self.user.username} in {self.server.name}"

class Message(models.Model):
    server = models.ForeignKey(Server, related_name="messages", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_at"]
