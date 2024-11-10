from django.db import models


class Cities(models.Model):
    city_ascii = models.TextField(null=False)
    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)
    country = models.TextField(null=False)

    def __str__(self):
        return self.city_ascii

    class Meta:
        db_table = "cities"
        managed = False
