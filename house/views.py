from django.shortcuts import render, Http404, HttpResponse
from .models import House
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
				houseInstance.participants.add = request.user
				houseInstance.save()
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404