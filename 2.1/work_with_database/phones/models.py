from django.db import models
from slugify import slugify

class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.URLField()
    release_date =models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, auto_created=name)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
