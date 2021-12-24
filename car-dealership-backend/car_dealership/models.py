from django.db import models


class Brand(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = True
        db_table = "brand"


class Client(models.Model):
    full_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, null=False)

    class Meta:
        managed = True
        db_table = "client"


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=None, null=False)
    id_client = models.ForeignKey(
        Client,
        on_delete=models.SET_DEFAULT,
        db_column="id_client",
        default=None,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50, null=False)
    new = models.BooleanField(default=True, null=False)
    doors = models.IntegerField(default=3, null=False)
    cubic_capacity = models.IntegerField(null=False)
    power = models.IntegerField(null=False)

    class Meta:
        managed = True
        db_table = "car"
