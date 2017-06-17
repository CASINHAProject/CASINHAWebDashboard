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
		return Response(serializer.data, status=status.HTTP_201_CREATED)
