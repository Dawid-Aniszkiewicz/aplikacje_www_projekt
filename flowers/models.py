from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nazwa kategorii")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug (URL)")
    description = models.TextField(blank=True, verbose_name="Opis kategorii")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"
        ordering = ['name']

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa kwiatu")
    latin_name = models.CharField(max_length=150, blank=True, verbose_name="Nazwa łacińska")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug (URL)")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="flowers",
        verbose_name="Kategoria"
    )
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="added_flowers",
        verbose_name="Dodane przez"
    )
    description = models.TextField(verbose_name="Opis")
    height_cm = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Wysokość (cm)"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0.00)],
        verbose_name="Cena (PLN)"
    )
    is_available = models.BooleanField(default=True, verbose_name="Dostępny")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ostatnia aktualizacja")

    class Meta:
        verbose_name = "Kwiat"
        verbose_name_plural = "Kwiaty"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.latin_name})" if self.latin_name else self.name