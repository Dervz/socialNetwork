import urllib3
import json

from django.shortcuts import render

API_URL = 'localhost:8000/api/'


def list_members(request):
	http = urllib3.PoolManager()
	profile_text_lower_than = 20 # Number of characters in profile

	response_members_list = http.request('GET', '{api_url}{endpoint}?profile__text={txt_lt}'.format(
		api_url=API_URL, 
		endpoint='member-list/',
		txt_lt=profile_text_lower_than
	))

	members_list = json.loads(response_members_list.data.decode('UTF-8'))
	return render(request, 'api_client/list_members.html', context={'members_list': members_list})


def list_messages(request):
	messages_list = {}

	if 'search' in request.GET.keys():
		http = urllib3.PoolManager()
		username = request.GET.get('search')

		response_messages_list = http.request('GET', '{api_url}{endpoint}?user__username={username}'.format(
			api_url=API_URL,
			endpoint='message-list/',
			username=username
		))

		messages_list = json.loads(response_messages_list.data.decode('UTF-8'))

	return render(request, 'api_client/list_messages.html', context={'messages_list': messages_list})