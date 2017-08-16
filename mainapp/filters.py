from django.db.models import Q
from django.db.models.functions import Length

from django_filters import rest_framework as filters
from django_filters.filters import EMPTY_VALUES

from .models import Member, Message


class LengthCharFilter(filters.CharFilter):
	"""
	Allows filtering by field content length.
	"""

	def filter(self, qs, value):
		if value in EMPTY_VALUES:
			return qs
		if self.distinct:
			qs = qs.distinct()
		
		qs = qs.annotate(**{'%s_length' % self.name: Length(self.name)})
		qs = qs.filter(
			Q(**{'%s_length__%s' % (self.name, self.lookup_expr): value}) | 
			Q(**{'%s__isnull' % self.name: True})
		)
		return qs


class MemberFilter(filters.FilterSet):
	profile__text = LengthCharFilter(lookup_expr='lt')

	class Meta:
		model = Member
		fields = ('profile__text',)


class MessageFilter(filters.FilterSet):
	user__username = filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Message
		fields = ('user__username',)