from datetime import timezone
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    datedenaissance = models.DateField()
    pseudo = models.CharField(max_length=100)
    motsdepasse = models.CharField(max_length=100)
    IDuser = models.AutoField(primary_key=True)

class Serveur(models.Model):
    nom = models.CharField(max_length=100)
    Permission = models.TextField()
    IDserveur = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nom
    
class Role(models.Model):
    nom = models.CharField(max_length=100)
    serveur = models.ForeignKey(Serveur, related_name="roles", on_delete=models.CASCADE)
    can_manage_roles = models.BooleanField(default=False)
    can_delete_messages = models.BooleanField(default=False)

    class Meta:
        unique_together = ("nom", "serveur")

    def __str__(self):
        return f"{self.nom} @ {self.serveur.nom}"
    
class Membership(models.Model):
    user = models.ForeignKey(User, related_name="memberships", on_delete=models.CASCADE)
    serveur = models.ForeignKey(Serveur, related_name="members", on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role, related_name="members", blank=True)
    joined_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("user", "server")

    def __str__(self):
        return f"{self.user.nom} in {self.server.nom}"

class Message(models.Model):
    server = models.ForeignKey(Serveur, related_name="messages", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_at"]

class gestionserveur(models.Model):
    idutilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    idserveur = models.ForeignKey(Serveur, on_delete=models.CASCADE)

class Demande(models.Model):
    libelé = models.CharField(max_length=100)
    statut = models.CharField(max_length=100)
    IDdemande = models.AutoField(primary_key=True)

class Amitier(models.Model):
    utilisateur1 = models.ForeignKey(User, related_name='utilisateur1', on_delete=models.CASCADE)
    utilisateur2 = models.ForeignKey(User, related_name='utilisateur2', on_delete=models.CASCADE)
    statut = models.BooleanField(default=False)

class Meta:
    unique_together = ('utilisateur1', 'utilisateur2')
    def __str__(self):
        self.statut = True
        self.save()
        return f"{self.utilisateur1.name} - {self.utilisateur2.name}"

