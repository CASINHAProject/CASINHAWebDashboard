from django.db import models
from django.contrib.auth.models import Permission, User

class ImageData(models.Model):
	user = models.ForeignKey(User, null=False, blank=False, related_name='+')
	profile = models.FileField(upload_to='profile/', null=True, blank=True)
	cover = models.FileField(upload_to='cover/', null=True, blank=True)
	
	def __str__(self):
		return 'Dados de ' + self.user.username