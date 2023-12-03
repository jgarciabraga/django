from django.db import models

# Create your models here.


class Cliente(models.Model):

    cpf = models.CharField(unique=True, null=False, blank=False, max_length=11)
    nome = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(unique=True, null=False, default='')
    data_nascimento = models.DateField(null=False, blank=False)
    is_ativo = models.BooleanField(null=False, default=True)
