from django.db import models

BRAND_CHOICES = (
    ('MERCEDES', 'Mercedes'),
    ('TESLA', 'Tesla'),
    ('TOYOTA', 'Toyota'),
    ('BMW', 'Bmw'),
    ('AUDI', 'Audi')
)

class Car(models.Model):
    brand = models.CharField(max_length=200, choices=BRAND_CHOICES)
    model = models.CharField(max_length=200)
    max_speed = models.PositiveIntegerField()
    country = models.CharField(max_length=200, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.brand, self.model, self.country)

    def save(self, *arg, **kwargs):
        if self.brand == 'TESLA':
            self.country = 'USA'
        elif self.brand == 'TOYOTA':
            self.country = 'JAPAN'
        else:
            self.country = 'Germany'
        super().save(*arg, **kwargs)


class Sale(models.Model):
    item = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return str(self.item)
