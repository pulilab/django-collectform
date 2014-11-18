import json
import unittest
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from collectform import models
from collectform import views

class TestCollectformView(unittest.TestCase):

    def setUp(self):
        models.DistributionRequests.objects.all().delete()
        self.requests = RequestFactory()
        self.user, created = User.objects.get_or_create(pk=1, username='doge', password='doge', email='doge@example.com', first_name='Mr')

    def tearDown(self):
        models.DistributionRequests.objects.all().delete()

    def test_minimum_data_fills_user(self):
        request = self.requests.post('/')
        request._user = self.user

        resp = csrf_exempt(views.handle_post)(request)
        assert resp.status_code == 200
        assert resp.data['status'] == 'success'

    def test_full_data(self):
        request = self.requests.post('/', data={
            'budget': 1000,
            'max_bid_per_view': 0.7,
            'campaign_start_date': '2014-11-10',
            'campaign_end_date': '2014-11-11',
            'gender_male': True,
            'gender_female': True,
            'age_group': '18-24',
            'location': 'Budapest, Hungary',
            'topics': 'tea, brownie',
            'urls': 'http://vidzor.com'
        })
        request._user = self.user

        resp = csrf_exempt(views.handle_post)(request)
        assert resp.status_code == 200
        assert resp.data['status'] == 'success'

    def test_with_vidzio(self):
        request = self.requests.post('/', {
            'vidzios': [1]
        })
        request._user = self.user

        resp = csrf_exempt(views.handle_post)(request)
        assert resp.status_code == 200
        assert resp.data['status'] == 'success'
        assert models.Vidzios.objects.count() == 1

