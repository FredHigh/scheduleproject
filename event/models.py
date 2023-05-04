from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    day = models.ForeignKey("weekday.Week", on_delete=models.CASCADE)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title
