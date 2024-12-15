from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50, choices=[
        ('HOT', 'Hot Coffee'),
        ('ICED', 'Iced Coffee'),
        ('SPECIAL', 'Specialty Coffee'),
    ])
    image = models.ImageField(upload_to='coffee_images/', blank=True, null=True)

    def __str__(self):
        return self.name
