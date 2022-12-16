from django.db import models


class AssurancePlan(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    bannier = models.ImageField(upload_to='bannier/')

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('main_app:plan', kwargs={'pk': self.pk})


class Partenaires(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="partenaire/")

    def __str__(self):
        return self.nom


class Testimonial(models.Model):
    nom = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)
    photo = models.ImageField(upload_to='cleint/', null=True, blank=True)

    def __str__(self):
        return self.nom


class Team(models.Model):
    nom = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to="team/", null=True, blank=True)
    fab = models.CharField(max_length=1000, null=True, blank=True)
    wht = models.CharField(max_length=1000, null=True, blank=True)
    twi = models.CharField(max_length=1000, null=True, blank=True)
    lin = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.nom
