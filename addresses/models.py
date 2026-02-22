"""
Docstring para addresses.models
"""
import re

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class State(models.Model):
    """
    Template for storing standard Brazilian states.
    This template can be used as a primary address or linked to other entities via ForeignKey.
    """
    name = models.CharField(_("Nome do Estado"), max_length=100)
    abbreviation = models.CharField(_("Sigla do Estado"), max_length=2)

    class Meta:
        verbose_name = _("Estado")
        verbose_name_plural = _("Estados")
        ordering = ["abbreviation"] 

    def __str__(self):
        return f'{self.abbreviation.upper()} ({self.name.title()})'


class City(models.Model):
    """
    Template for storing Brazilian standard cities.
    This template can be used as a primary address or related to other entities via ForeignKey.
    """
    name = models.CharField(_("Nome da Cidade"), max_length=100)
    state = models.ForeignKey(
        State,
        verbose_name=_("Estado"),
        on_delete=models.CASCADE,
        related_name="cities",
    )

    class Meta:
        verbose_name = _("Cidade")
        verbose_name_plural = _("Cidades")
        ordering = ["name"]

    def __str__(self):
        return f'{self.name} - {self.state.abbreviation}'

class Address(models.Model):
    """
    Template for storing standard Brazilian addresses.
    This template can be used as a primary address or related to other entities via ForeignKey.
    """
    streetsuffixes_choices = [
        ("Rua", _("Rua")),
        ("Avenida", _("Avenida")),
        ("Alameda", _("Alameda")),
        ("Travessa", _("Travessa")),
        ("Praça", _("Praça")),
        ("Largo", _("Largo")),
        ("Viela", _("Viela")),
        ("Estrada", _("Estrada")),
        ("Rodovia", _("Rodovia")),
    ]
    street_suffix = models.CharField(
        _("Tipo de Logradouro"),
        max_length=20,
        choices=streetsuffixes_choices,
    )
    street_name = models.CharField(_("Endereço"), max_length=255)
    neighborhood = models.CharField(_("Bairro"), max_length=255)
    zip_code = models.CharField(
        _('CEP'),
        max_length=9,
        validators=[RegexValidator(r'^\d{5}-\d{3}$', 'CEP deve estar no formato 00000-000.')]
    )
    city = models.ForeignKey(
        City,
        verbose_name=_("Cidade"),
        on_delete=models.CASCADE,
        related_name="addresses",
    )

    class Meta:
        verbose_name = _("Endereço")
        verbose_name_plural = _("Endereços")
        ordering = ["street_name"]

    def __str__(self):
        return f'{self.zip_code} - {self.street_suffix} {self.street_name} - {self.neighborhood}, {self.city}'

    def clean(self):
        """It normalizes the postal code to the standard Brazilian format."""
        if self.zip_code:
            zipcode_clean = re.sub(r'[^0-9]', '', self.zip_code)
            if len(zipcode_clean) == 8:
                self.zip_code = f'{zipcode_clean[:5]}-{zipcode_clean[5:]}'
