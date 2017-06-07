from django.db import models
from django.utils import timezone

from house.models import House

class Actuator(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nome', null=False, blank=False)
	crated_by = models.DateTimeField(default=timezone.now)
	topic = models.CharField(max_length=100, verbose_name='Tópico', null=False, blank=False)
	house = models.ForeignKey(House, verbose_name='Casa correspondente')

	def __str__(self):
		return self.name