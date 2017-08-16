from .models import Member, Message, Profile

from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('text',)


class MemberSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Member
		fields = ('username', 'profile', 'following')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Message
		fields = ('user', 'recip', 'pm', 'time', 'text')