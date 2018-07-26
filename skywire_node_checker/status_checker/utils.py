import datetime
import requests
from django.conf import settings
from skywire_node_checker.status_checker.models import Uptime, Node

# Dicotomic search O(log n)
def get_node_position(a, c):
    if a[0].key > c:
        return False
    else:
        low, hi = 0, len(a)
        if a[low].key == c: return low
        while low + 1 != hi:
            mid = low + ((hi - low) // 2)
            if a[mid].key == c:
                return mid
            elif a[mid].key < c:
                low = mid
            else:
                hi = mid
    return False

def new_node(key, start_time, actual_datetime):
    n = Node(key=key)
    n.last_checked = actual_datetime
    n.save()
    u = Uptime(node=n, start_time=start_time)
    u.save()
    active_date = u.created_at.replace(tzinfo=None) + datetime.timedelta(0, u.start_time)
    if active_date > actual_datetime:
        u.created_at = actual_datetime - datetime.timedelta(0, u.start_time)
        u.save()

def update_uptime(n, start_time, actual_datetime):
    u = Uptime.objects.filter(node=n)
    u = u.order_by('-created_at')[0]
    if start_time > u.start_time:
        u.start_time = start_time
        u.save()
    # Create a new period if between refresh the node has been restarted
    else:
        u = Uptime(node=n, start_time=start_time)
        u.save()
        active_date = u.created_at.replace(tzinfo=None) + datetime.timedelta(0, u.start_time)
        if active_date > actual_datetime:
            u.created_at = actual_datetime - datetime.timedelta(0, u.start_time)
            u.save()

def do_request():
    url = settings.API_URL
    r = requests.get(url)
    return r.json()

def autoupdate():
    node_list=do_request()
    all_ordered_nodes_db = Node.objects.all().order_by("key")
    # print (all_ordered_nodes_db)
    actual_datetime = datetime.datetime.now()
    for node in node_list:
        if all_ordered_nodes_db.count() > 0:
            position = get_node_position(all_ordered_nodes_db, node['key'])
            # If node does not exist then create it
            if not position and position is not 0:
                new_node(node['key'], node['start_time'], actual_datetime)
            else:
                n = all_ordered_nodes_db[position]
                # If node exist and is online then update start_time
                if n.online:
                    update_uptime(n, node['start_time'], actual_datetime)
                else:
                    # If node exist and is offline then turn it online and create new uptime period.
                    n.online = True
                    update_uptime(n, node['start_time'], actual_datetime)
                n.last_checked = actual_datetime
                n.save()
        else:
            new_node(node['key'], node['start_time'], actual_datetime)
            # If node has not been last_checked then is offline
    offline_node_list = Node.objects.exclude(last_checked=actual_datetime)
    for offline_node in offline_node_list:
        offline_node.online = False
        offline_node.last_checked = actual_datetime
        offline_node.save()

    nodes_checked = Node.objects.all().count()
    nodes_online = Node.objects.filter(online=True).count()

    return nodes_checked, nodes_online
