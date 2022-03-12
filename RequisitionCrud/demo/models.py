from django.db import models


class User(models.Model):
    """
    """
    objects = None
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150, unique=True)
    age = models.CharField(max_length=150)
    mobileNo = models.CharField(max_length=16)
    password = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "um_user"


class Subcatogory(models.Model):
    """
    """
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = "um_Subcatogory"


class Catogory(models.Model):
    """
    """
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=256, blank=True, null=True)
    subcategory = models.ForeignKey('Subcatogory', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "um_Catogory"
