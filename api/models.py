from django.db import models


class Geeks(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    role = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="https://icedrive.net/1/05umfBtS3a", null=True, blank=True)

