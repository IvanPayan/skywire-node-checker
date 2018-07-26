# -*- coding: utf-8 -*-
from django.shortcuts import render
from skywire_node_checker.status_checker import utils
from skywire_node_checker.status_checker.features import node_search, online_node_rank
from django.conf import settings


def index(request):
    node_list, show_form = node_search.node_search(request)
    context = {'node_list': node_list, 'show_form': show_form, 'min_uptime_percent':settings.MIN_UPTIME_PERCENT,'google_id':settings.GOOGLE_ANALYTICS_ID}
    return render(request, 'online_checker/index.html', context)


def update(request):
    nodes_checked, nodes_online = utils.autoupdate()
    context = {'nodes_checked': nodes_checked, 'nodes_online': nodes_online}
    return render(request, 'online_checker/update.html', context)


def online_uninterruptedly(request):
    rank_list = online_node_rank.online_node_rank(100)
    context = {'rank_list': rank_list}
    return render(request, 'online_checker/online_uninterruptedly.html', context)
