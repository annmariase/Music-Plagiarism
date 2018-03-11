# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import signup, Track

# Register your models here.
admin.site.register(signup)
admin.site.register(Track)