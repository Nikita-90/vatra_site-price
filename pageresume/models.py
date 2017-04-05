from django.db import models

class StatiscticsHit(models.Model):
    ip_client = models.CharField(max_length=50)
    link_client = models.TextField()
    date_client = models.DateTimeField()

    def __str__(self):
        return str(self.ip_client)
