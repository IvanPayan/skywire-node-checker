import datetime

from skywire_node_checker.status_checker.models import Uptime


def online_node_rank(top_n):
    rank_list = Uptime.objects.filter(node__online=True).order_by('node__key', '-created_at')
    actual_pub_key = 0
    last_period_list = []
    # Get last periode of each online node
    for uptime in rank_list:
        if actual_pub_key != uptime.node.key:
            actual_pub_key = uptime.node.key
            uptime.start_time_hours = str(datetime.timedelta(seconds=uptime.start_time))
            last_period_list.append(uptime)
    rank_list = sorted(last_period_list, key=lambda x: x.start_time, reverse=True)[:top_n]
    return rank_list
