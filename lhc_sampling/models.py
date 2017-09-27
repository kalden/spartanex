# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class LHC_Sampling_Settings(models.Model):
    #filepath = models.CharField(max_length=100)
    parameters = models.TextField()
    numberOfSamples = models.FloatField()
    minimumValues = models.CharField(max_length=100)
    maximumValues = models.CharField(max_length=100)
    NORMAL = 'normal'
    OPTIMAL = 'optimal'
    algorithm_choices = (
        ( NORMAL, 'normal'),
        ( OPTIMAL,'optimal'),
    )

    algorithm = models.CharField(max_length=9,
                  choices=algorithm_choices,
                  default="normal")
