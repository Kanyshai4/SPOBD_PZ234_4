from django.db import models

# Create your models here.

class Professia(models.Model):
    title = models.TextField(max_length=50,verbose_name="Название")
    class Meta:
        ordering=["-title"]
        verbose_name="Профессия"
        verbose_name_plural = "Профессии"
    def __str__(self):
        return self.title
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Professia._meta.fields]
