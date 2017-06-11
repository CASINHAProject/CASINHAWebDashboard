from django.shortcuts import render, Http404, HttpResponse, get_object_or_404
from .models import House, Message
from core.models import User
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
	get_object_or_404(house.participants, pk=request.user.pk)
	messages = Message.objects.filter(house=house)[::-1]
	return render(request, 'house_detail.html', {
		'house':house,
		'messages':messages
		})

def house_participants(request, pk):
	house = get_object_or_404(House, pk=pk)
	get_object_or_404(house.participants, pk=request.user.pk)
	participants = house.participants.values()
	return render(request, 'house_participants.html', {
		'house':house,
		'participants':participants
		})

def addMessage(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('message') != "":
				print(request.POST.get('message'))
				print(request.POST.get('house'))
				messageInstance = Message()
				messageInstance.text = request.POST.get('message')
				messageInstance.creator = request.user
				messageInstance.house = get_object_or_404(House, pk=request.POST.get('house'))
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