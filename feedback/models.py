# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Feedback(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    class Meta:
        managed = False
        db_table = 'test_whitealbum'
