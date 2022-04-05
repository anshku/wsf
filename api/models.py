from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

Positions = [
    ('Goalkeeper', 'Goalkeeper'),
    ('Defender', 'Defender'),
    ('Midfielder', 'Midfielder'),
    ('Forward', 'Forward')
]

class Player(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(choices=Positions, max_length=100)
    odds = models.FloatField()
    margin = models.FloatField(default=0.1, validators=[MinValueValidator(0.01), MaxValueValidator(1.0)])

    class Meta:
        ordering = ['id']
