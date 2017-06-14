from django.shortcuts import render, HttpResponse, redirect, Http404, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, ImageData
from house.models import House, Message
import json

@login_required(login_url='/login')
def index(request):
	myhouses = House.objects.filter(creator=request.user)
	myhousespart = House.objects.filter(participants=request.user).exclude(creator=request.user)
	mymessages = Message.objects.filter(creator=request.user)

	return render(request, 'index.html',{
		'myhouses':myhouses,
		'myhousespart':myhousespart,
		'mymessages':mymessages[::-1][0:10]
		})

def login_page(request):
	if request.user.is_authenticated(): return index(request)
	return render(request, 'login.html')

def entrar(request):
	if request.method == 'POST' and request.is_ajax():
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404


def register(request):
	if request.method == 'POST' and request.is_ajax():
		userInstance = User()
		userInstance.username = request.POST.get('username')
		userInstance.email = request.POST.get('email')
		passw = request.POST.get('password')
		userInstance.set_password(passw)
		userInstance.save()
		print("user: "+ userInstance.username)
		print("senha: "+ passw)
		new_image_data = ImageData()
		new_image_data.user = userInstance
		new_image_data.save()
		user = authenticate(username=userInstance.username, password=passw)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def make_logout(request):	
	logout(request)
	return redirect("/")

def deletaconta(request):
	if request.is_ajax():
		get_object_or_404(ImageData, user=request.user).delete()
		request.user.delete()
		return HttpResponse(json.dumps(True), content_type="application/json")
	raise Http404

def edit_profile(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('username') != "" and request.POST.get('email') != "":
				#print(request.POST.get('name') + request.POST.get('server') + request.POST.get('user') + request.POST.get('password') + request.POST.get('portws'))

				request.user.username = request.POST.get('username')
				request.user.email = request.POST.get('email')
				request.user.save()
				dataimage = get_object_or_404(ImageData, user=request.user)
				dataimage.profile = request.FILES.get('profile')
				dataimage.cover = request.FILES.get('cover')
				dataimage.save()
				#houseInstance.save()
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404