from django.db import models
from django.utils import timezone

from house.models import House

ACTUATOR_TYPES = (
    (1, 'Lâmpada'),
    (2, 'Sonar'),
    (3, 'Temperatura'),
    (4, 'Ventilador'),
    (5, 'Outro'),
)

class Actuator(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nome', null=False, blank=False)
	description = models.CharField(max_length=100, verbose_name='Descrição', null=False, blank=False)
	crated_by = models.DateTimeField(default=timezone.now)
	actuator_type = models.IntegerField(choices=ACTUATOR_TYPES, null=False, default=1)
	topic = models.CharField(max_length=100, verbose_name='Tópico', null=False, blank=False)
	house = models.ForeignKey(House,  related_name='actuators', verbose_name='Casa correspondente')

	def __str__(self):
		return self.name