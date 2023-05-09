from django.db import models

class Week(models.Model):
    week_id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.day