from rest_framework import generics

from .models import Member, Message, Profile
from .filters import MemberFilter, MessageFilter
from .serializers import MemberSerializer, MessageSerializer, ProfileSerializer


class MemberList(generics.ListAPIView):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer
	filter_class = MemberFilter


class MemberRetrieve(generics.RetrieveAPIView):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer


class ProfileRetrieve(generics.RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer


class MessageList(generics.ListAPIView):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
	filter_class = MessageFilter