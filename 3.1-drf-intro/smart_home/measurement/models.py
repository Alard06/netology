from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    """Датчик"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)


class Measurement(models.Model):
    """Измерения"""
    sensor = models.ForeignKey(Sensor,
                           on_delete=models.CASCADE,
                               related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
