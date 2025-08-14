from django.db import models

class Locataire(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Loyer(models.Model):
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mois = models.CharField(max_length=20)  # exemple: "Janvier 2025"
    date_paiement = models.DateField()

    def __str__(self):
        return f"{self.locataire.nom} - {self.mois}"

