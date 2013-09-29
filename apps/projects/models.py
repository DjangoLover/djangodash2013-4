from django.conf import settings
from django.db import models
from uuslug import uuslug


class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, start_no=2)
        super(Project, self).save(*args, **kwargs)


