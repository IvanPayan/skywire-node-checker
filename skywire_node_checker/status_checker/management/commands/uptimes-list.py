from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from skywire_node_checker.status_checker.models import Node


class Command(BaseCommand):
    help = 'List of uptimes'
    min_uptime_percentage = 75

    def add_arguments(self, parser):
        parser.add_argument('date',
                            type=str,
                            help="Month to pick uptimes (format Y-m)")

    def get_month_seconds(self):
        return 3600 * 24 * 30

    def handle(self, *args, **options):
        date = datetime.strptime(options.get('date'), "%Y-%m")

        queryset = Node.objects \
            .filter(uptime__created_at__year=date.year, uptime__created_at__month=date.month) \
            .distinct('key')

        print("key\tuptime\tuptime percentage")
        for node in queryset.all():
            total_uptime = node.get_uptime(date)
            uptime_percentage = round(float(total_uptime) / float(self.get_month_seconds()) * 100, 2)

            print("{}\t{}\t{}".format(node.key, total_uptime, uptime_percentage))
