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


class Person(models.Model):
    person = models.CharField(max_length=100)
    region = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.person} - {self.region}"


class Order(models.Model):
    row_id = models.IntegerField()
    order_id = models.CharField(max_length=20)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    segment = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    region = models.CharField(max_length=50)
    product_id = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=200)
    sales = models.FloatField()
    quantity = models.IntegerField()
    discount = models.FloatField()
    profit = models.FloatField()

    def __str__(self):
        return f"Order {self.order_id} - {self.product_name} ({self.customer_name})"
