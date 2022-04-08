import datetime

from django.test import TestCase
from django.utils import timezone

from .models import User


class UserModelTests(TestCase):

	def test_was_published_recently_with_future_user(self):
		"""
		was_published_recently() returns False for questions whose pub_date
		is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_user = User(start_date=time)
		self.assertIs(future_user.was_published_recently(), False)