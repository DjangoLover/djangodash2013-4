from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.admin import UserAdmin
from django.db import models
from apps.utils.gravatar import get_gravatar_link

class KantaskerUser(AbstractUser):
    avatar = models.URLField(
        name='avatar',
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.email:
            gravatar_url = get_gravatar_link(email=self.email)
        else:
            gravatar_url = get_gravatar_link(email=None)
        self.avatar = gravatar_url
        super(KantaskerUser, self).save(*args, **kwargs)


admin.site.register(KantaskerUser, UserAdmin)



