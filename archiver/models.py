from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

class ArchiverApp(models.Model):
    name = models.CharField(max_length=50)
    app_label = models.CharField(max_length=50)
    description = models.TextField()
    public = models.BooleanField()
    creators = models.ManyToManyField(User, related_name='archiver_apps')

    def __unicode__(self):
        return self.name

    def get_models(self):
        return ContentType.objects.filter(app_label=self.app_label)
    
    def get_permissions(self):
        return [(model, Permission.objects.filter(content_type=model)) for model in self.get_models()]
