from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^members-list/$', views.list_members, name='members_list'),
	url(r'^messages-list/$', views.list_messages, name='messages_list')
]