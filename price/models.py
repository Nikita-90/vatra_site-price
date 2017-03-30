from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class LoadingFile(models.Model):
    file = models.FileField()

    def __str__(self):
        return str(self.file)


class Price(models.Model):
    loadingfile = models.ForeignKey(LoadingFile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    name_views = models.CharField(max_length=100)
    cost = models.FloatField()

    def __str__(self):
        return str(self.name_views)


@receiver(pre_delete, sender=LoadingFile)
def loadingfile_delete(sender, instance, **kwargs):
    instance.file.delete(False)
