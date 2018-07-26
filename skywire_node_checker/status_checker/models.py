from django.db import models
from django.db.models import Sum


class Node(models.Model):
    def __str__(self):
        return "key: {0}, online: {1}, last_checked: {2}".format(self.key, self.online, self.last_checked)

    key = models.CharField(max_length=128)
    online = models.BooleanField(default=True)
    last_checked = models.DateTimeField()

    def get_last_uptime(self, date):
        return self.uptime_set \
            .filter(created_at__year=date.year, created_at__month=date.month).order_by('id').last()

    def get_uptime(self, date):
        date = date.replace(day=1)

        uptimes_queryset = self.uptime_set \
            .filter(created_at__year=date.year, created_at__month=date.month)

        total_uptime = uptimes_queryset.aggregate(Sum('start_time'))['start_time__sum']

        return total_uptime


class Uptime(models.Model):
    def __str__(self):
        return "node: {0}, start_time: {1}, created_at: {2}".format(self.node.key, self.start_time, self.created_at)

    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    start_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
