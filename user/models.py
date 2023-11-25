from django.db import models
from django.contrib.auth.models import AbstractUser
from mPersona.models import mPersona

class User(AbstractUser):
    picture = models.ImageField(default='default_image.jpg', upload_to='users/')
    cvPersona = models.ForeignKey(mPersona, on_delete=models.DO_NOTHING, null=True, blank=False)
    dateEnd = models.DateTimeField(null=True, blank=False)
    username = models.CharField(max_length=20, null=True, blank=False, unique=True)