from django.shortcuts import render
from django.shortcuts import get_object_or_404
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializer import HouseSerializer
from house.models import House

from actuator.models import Actuator

from django.contrib.auth import login, logout, authenticate

class ActuatorsListView(APIView):
	'''
	Envie username, senha e chave de acesso e retornará
	Todos os atuadores e sensores de um ambiente

	Exemplo:

	{
     "user": "...",
     "pass": "...",
     "token":"..."
	}
	'''

	def post(self, request, format=None):
		print(request.data['user'])
		hash_key = request.data['token']
		house = get_object_or_404(House, hash_key=hash_key)
		user = authenticate(username=request.data['user'], password=request.data['pass'])
		if user is None:
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

		get_object_or_404(house.participants, pk=user.pk)

		serializer = HouseSerializer(house)
		return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateLocalizationView(APIView):
	'''
	Envie key da casa, latitude e longitude e altere a localização
	do ambiente.

	Exemplo:

	{
     "key": "...",
     "latitude": "...",
     "longitude":"..."
	}
	'''

	def post(self, request, format=None):
		hash_key = request.data['key']
		house = get_object_or_404(House, hash_key=hash_key)
		if request.data['key'] == "" or request.data['latitude'] == "" or request.data['longitude'] == "":
			return Response({"message":"404 Not Found"}, status=status.HTTP_404_NOT_FOUND)
		house.latitude = request.data['latitude']
		house.longitude = request.data['longitude']
		house.save()

		return Response(house.hash_key, status=status.HTTP_200_OK)