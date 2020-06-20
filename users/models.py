from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user           = models.OneToOneField(
                        User,
                        on_delete=models.CASCADE
    )
    is_available    = models.BooleanField(default = True)
    available_since = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return f'{self.user.username}'

    def get_username(self):
        return str(self.user.username )
