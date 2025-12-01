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
    statut = models.CharField(max_length=100)