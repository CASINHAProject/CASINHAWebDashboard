from django.shortcuts import render, Http404, HttpResponse, get_object_or_404
from .models import House, Message
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


def house_detail(request, pk):
	house = get_object_or_404(House, pk=pk)
	messages = Message.objects.filter(house=house)[::-1]
	return render(request, 'house_detail.html', {
		'house':house,
		'messages':messages
		})
