# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from skywire_node_checker.status_checker.models import Node, Uptime

admin.site.register(Node)
admin.site.register(Uptime)
