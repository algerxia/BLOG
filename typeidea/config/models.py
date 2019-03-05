from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL,"正常"),
        (STATUS_DELETE,"删除"),
    )
