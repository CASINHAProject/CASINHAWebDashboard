from django.shortcuts import render, Http404, HttpResponse, get_object_or_404
from .models import House, Message
from core.models import User
from actuator.models import Actuator

import json

def add(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('name') != "":
				print(request.POST.get('name') + request.POST.get('server') + request.POST.get('user') + request.POST.get('password') + request.POST.get('portws'))
				houseInstance = House()
				houseInstance.name = request.POST.get('name')
				houseInstance.server = request.POST.get('server')
				houseInstance.user = request.POST.get('user')
				houseInstance.password = request.POST.get('password')
				houseInstance.portws = request.POST.get('portws')
				houseInstance.image = request.FILES.get('image')
				houseInstance.creator = request.user
				houseInstance.save()
				houseInstance.participants.add(request.user)
				#houseInstance.save()
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404


def house_detail(request, pk):
	house = get_object_or_404(House, pk=pk)
	actuators = Actuator.objects.filter(house=house)
	get_object_or_404(house.participants, pk=request.user.pk)
	messages = Message.objects.filter(house=house)[::-1]
	participants = house.participants.values()
	actuators = Actuator.objects.filter(house=house)
	return render(request, 'house_detail.html', {
		'house':house,
		'messages':messages,
		'actuators':actuators,
		'participants':participants
		})

def house_participants(request, pk):
	house = get_object_or_404(House, pk=pk)
	get_object_or_404(house.participants, pk=request.user.pk)
	participants = house.participants.get_queryset()
	actuators = Actuator.objects.filter(house=house)
	return render(request, 'house_participants.html', {
		'house':house,
		'participants':participants,
		'actuators':actuators
		})

def house_actuators(request, pk):
	house = get_object_or_404(House, pk=pk)
	get_object_or_404(house.participants, pk=request.user.pk)
	participants = house.participants.values()
	actuators = Actuator.objects.filter(house=house)

	return render(request, 'house_actuators.html', {
		'house':house,
		'actuators':actuators,
		'participants':participants
		})

def addMessage(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('message') != "":
				print(request.POST.get('message'))
				print(request.POST.get('house'))
				print(request.POST.get('is_m'))
				messageInstance = Message()
				messageInstance.text = request.POST.get('message')
				messageInstance.creator = request.user
				messageInstance.house = get_object_or_404(House, pk=request.POST.get('house'))
				if request.POST.get('is_m') == '1':
					print("é m")
					messageInstance.is_message = True
				messageInstance.save()
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def search_users(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('message') != "" and request.POST.get('house') != "":
				argument = request.POST.get('message')
				ambient = request.POST.get('house')
				house = get_object_or_404(House, pk=ambient)
				if house.creator != request.user: raise Http404
				users = User.objects.filter(username__icontains=argument).exclude(pk__in=[i['pk'] for i in list(house.participants.values('pk'))])
				print(users)
				return HttpResponse(json.dumps(list(users.values('username','pk', 'email'))), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def add_user(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('iduser') != "" and request.POST.get('house') != "":
				ambient = request.POST.get('house')
				user = request.POST.get('iduser')
				house = get_object_or_404(House, pk=ambient)
				if house.creator != request.user: raise Http404
				house.participants.add(user)
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def remove_user(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('iduser') != "" and request.POST.get('house') != "":
				ambient = request.POST.get('house')
				user = request.POST.get('iduser')
				house = get_object_or_404(House, pk=ambient)
				if house.creator != request.user: raise Http404
				house.participants.remove(user)
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def delete_house(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('house') != "":
				ambient = request.POST.get('house')
				house = get_object_or_404(House, pk=ambient).delete()
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def add_actuator(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('name') != "" and request.POST.get('topic') != "" and request.POST.get('desc') != "" and request.POST.get('idactuator') != "" and request.POST.get('idhouse') != "":
				ambient = request.POST.get('idhouse')
				name = request.POST.get('name')
				topic = request.POST.get('topic')
				desc = request.POST.get('desc')
				type_actuator = request.POST.get('idactuator')
				house = get_object_or_404(House, pk=ambient)
				if house.creator != request.user: raise Http404
				new = Actuator(name=name, description=desc,actuator_type=type_actuator, topic=topic, house=house)
				new.save()
				
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def remove_actuator(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('actuator') != "" and request.POST.get('house') != "":
				ambient = request.POST.get('house')
				actuator = request.POST.get('actuator')
				house = get_object_or_404(House, pk=ambient)
				if house.creator != request.user: raise Http404
				get_object_or_404(Actuator, pk=actuator).delete()
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404