#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-collectform
------------

Tests for `django-collectform` models module.
"""

from datetime import date
import os
import shutil
import unittest

from django.contrib.sites.models import Site
from collectform import models


class TestCollectform(unittest.TestCase):

    def setUp(self):
        pass

    def test_required_data_works(self):
        dr = models.DistributionRequests.objects.create(
            name='Doge',
            email='doge@example.com',
        )
        assert dr.pk
        assert dr.gender_male == False
        assert dr.gender_female == False
        assert dr.age_group == 'All'
        assert dr.location == 'All'
        assert dr.topics == ''
        assert dr.urls == ''

    def test_all_data(self):
        dr = models.DistributionRequests.objects.create(
            name='Doge',
            email='doge@example.com',
            username='doge',
            budget = 1000,
            max_bid_per_view = 0.7,
            campaign_start_date = date(2014, 11, 10),
            campaign_end_date = date(2014, 11, 11),
            gender_male = True,
            gender_female = True,
            age_group = '18-24',
            location = 'Budapest, Hungary',
            topics = 'tea, brownie',
            urls = 'http://vidzor.com'
        )
        assert dr.pk

    def test_with_vidzio(self):
        site = Site.objects.get(pk=1)
        dr = models.DistributionRequests.objects.create(
            name='Doge',
            email='doge@example.com',
        )
        dr.vidzios.create(vidzio=site)
        assert dr.vidzios.count() == 1

    def tearDown(self):
        pass
