from rest_framework import serializers
from house.models import House
from actuator.models import Actuator

class ActuatorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Actuator
		depth = 1
		fields = ['id', 'name', 'description', 'actuator_type', 'topic']

class HouseSerializer(serializers.ModelSerializer):

	actuators = ActuatorSerializer(many=True, read_only=True)

	class Meta:
		model = House
		depth = 1
		fields = ['id', 'name', 'creator', 'server', 'user', 'password', 'portws', 'actuators', 'image', 'hash_key']