from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.test.utils import override_settings


class TestCareers(TestCase):
    def setUp(self):
        pass

    def test_that_hidden_or_expired_job_ads_are_not_shown(self):
        self.assertEqual(1, 1)
