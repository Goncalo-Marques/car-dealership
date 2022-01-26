from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# brand model
class Brand(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = True
        db_table = "brand"

    def __str__(self):
        return f"{self.name}"


# client model
class Client(AbstractBaseUser, PermissionsMixin):
    # auth
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # details
    full_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "birthdate", "phone_number", "address"]

    objects = CustomUserManager()

    class Meta:
        managed = True
        db_table = "client"

    def __str__(self):
        return f"{self.email}"


# car model
class Car(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, db_column="brand", default=None, null=False
    )
    id_client = models.ForeignKey(
        Client,
        on_delete=models.SET_DEFAULT,
        db_column="id_client",
        default=None,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50, null=False)
    image_url = models.TextField(null=False)
    new = models.BooleanField(default=True, null=False)
    doors = models.IntegerField(default=3, null=False)
    cubic_capacity = models.IntegerField(null=False)
    power = models.IntegerField(null=False)

    class Meta:
        managed = True
        db_table = "car"

    def __str__(self):
        return f"{self.name}"
