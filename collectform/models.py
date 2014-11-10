# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from model_utils.models import TimeStampedModel
from model_utils import Choices


class DistributionRequests(TimeStampedModel):

    name = models.CharField(verbose_name='Contact name', max_length=255)
    email = models.EmailField(verbose_name='Contact e-mail')
    username = models.CharField(verbose_name='Contact user login', max_length=255, blank=True)
    budget = models.IntegerField(verbose_name='Budget in USD', blank=True, default=-1)
    max_bid_per_view = models.FloatField(verbose_name='Max. bid per view', default=-1, blank=True)
    campaign_start_date = models.DateField(verbose_name='Campaign start date', blank=True, null=True)
    campaign_end_date = models.DateField(verbose_name='Campaign end date', blank=True, null=True)
    gender_male = models.BooleanField(verbose_name='Target males', default=False)
    gender_female = models.BooleanField(verbose_name='Target females', default=False)
    age_group = models.CharField(verbose_name='Target age group', max_length=255, default="All")
    location = models.TextField(verbose_name='Target location', default='All')
    topics = models.TextField(verbose_name='Target topics', default='')
    urls = models.TextField(verbose_name='Topic proxy urls', default='')


class Vidzios(models.Model):
    request = models.ForeignKey(DistributionRequests, related_name='vidzios')
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    vidzio = generic.GenericForeignKey('content_type', 'object_id')
