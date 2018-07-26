import datetime, time

from skywire_node_checker.status_checker.models import Uptime, Node


def is_form_filled(request):
    # If the form is filled, hide the form and return a pub key list
    if 'key_list' in request.GET:
        string = request.GET['key_list']
        my_public_key_list = [x.strip() for x in string.split(',')]
        show_form = False
    # If not, show the form and return and empty list
    else:
        show_form = True
        my_public_key_list = []

    return my_public_key_list, show_form


def node_search(request):
    my_public_key_list, show_form = is_form_filled(request)

    node_list = []
    # For each pub key, give me the status, the last period duration and the total uptime of the actual month
    for pub_key in my_public_key_list:
        if Node.objects.filter(key=pub_key).count() > 0:
            n = Node.objects.get(key=pub_key)
            n.results = True
            n.last_period_time = Uptime.objects.filter(node=n).order_by('-id')[0].start_time
            n.last_period_time_hours = str(datetime.timedelta(seconds=n.last_period_time))
            today = n.last_checked.replace(tzinfo=None)

            # Seconds since 1st of the actual month at 0:00 am (GMT)
            month_start = datetime.datetime(today.year, today.month, 1, 0, 0)
            total_uptime = 0
            total_downtime = 0
            first_period_past_month = True
            last_period_actual_month = None

            periods_list = Uptime.objects.filter(node=n).order_by('-id')
            for period in periods_list:
                # Get the total time from the sum of each period of the actual month
                if period.created_at.month == today.month and period.created_at.year == today.year:
                    total_uptime = total_uptime + period.start_time
                    last_period_actual_month = period

                # Plus the part of the time from the last past month period that belongs to the actual one
                elif first_period_past_month:
                    # If node has actual month periods
                    if last_period_actual_month is not None:
                        seconds_between_periods = (last_period_actual_month.created_at - period.created_at).seconds + (
                            last_period_actual_month.created_at - period.created_at).days * 86400  # 86400 = num seconds in 1 day
                        if seconds_between_periods < period.start_time:
                            total_downtime = 0
                        else:
                            total_downtime = seconds_between_periods - period.start_time
                        actual_month_time = (last_period_actual_month.created_at.replace(
                            tzinfo=None) - month_start).seconds + (last_period_actual_month.created_at.replace(
                            tzinfo=None) - month_start).days * 86400 - total_downtime

                    else:
                        # If node has not actual month periods
                        active_date = period.created_at.replace(tzinfo=None) + datetime.timedelta(0, period.start_time)
                        if active_date <= month_start:
                            actual_month_time = 0
                        else:
                            actual_month_time = (active_date - month_start).seconds + (
                                active_date - month_start).days * 86400

                    if actual_month_time < 0:
                        actual_month_time = 0
                    total_uptime = total_uptime + actual_month_time
                    first_period_past_month = False
            n.total_uptime = total_uptime
            n.total_uptime_hours = str(datetime.timedelta(seconds=total_uptime))

            # Get seconds from the beggining of the actual month
            seconds_month_start = (today - month_start).seconds + (today - month_start).days * 86400
            n.uptime_percentage = round(float(total_uptime) / float(seconds_month_start) * 100, 2)
            if n.uptime_percentage > 100:
                n.uptime_percentage = float(100)
        else:
            n = Node()
            n.text = "No results for the public key: " + pub_key
            n.results = False
        node_list.append(n)
    return node_list, show_form
