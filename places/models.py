from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    #imgs = models.Imagefield()
    description_short = models.TextField(verbose_name="Короткое описание")
    description_long = models.TextField(verbose_name="Полное описание",
                                        blank=True, null=True)
    lng = models.FloatField(verbose_name="Долгота",
                            blank=True, null=True)
    lat = models.FloatField(verbose_name="Широта",
                            blank=True, null=True)
    
    def __str__(self):
        return self.title