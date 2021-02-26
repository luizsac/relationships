from django.contrib.auth import get_user_model
from django.db import models


class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self) -> models.CharField:
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self) -> models.CharField:
        return self.nome


def set_default_montadora(self) -> object:
    return Montadora.objects.get_or_create(nome="Padrão")[0]  # get_or_create retorna um objeto e um boolean


class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    # montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)  # um para muitos não fica explícito
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))  # on_delete usando SET
    modelo = models.CharField('Modelo', max_length=30)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    motoristas = models.ManyToManyField(get_user_model())

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self) -> str:
        return f'{self.montadora} {self.modelo}'


