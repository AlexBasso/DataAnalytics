from django.db import models


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
