from datetime import datetime

from django.test import TestCase

from skywire_node_checker.status_checker.models import Node, Uptime


class NodeTestCase(TestCase):
    last_checked = datetime(2018, 1, 1)
    key_1 = "02a30a4684e915dc5b8225ad105ca2c9c2844a97982d3d0042e856670fb1285512"
    key_2 = "020907316c650dcc89629f8a1960e2309228d31718da41274f67b4c947d1006f68"
   

    def setUp(self):
        Node.objects.create(key=self.key_1, online=True, last_checked=self.last_checked)
        Node.objects.create(key=self.key_2, online=False, last_checked=self.last_checked)

    def test_get_key(self):
        node = Node.objects.get(key=self.key_1)
        self.assertEqual(node.key, self.key_1)

    def test_set_key(self):
        node = Node.objects.get(key=self.key_1)
        node.key = "new_key"
        self.assertEqual(node.key, "new_key")

    def test_get_online(self):
        node = Node.objects.get(key=self.key_1)
        self.assertTrue(node.online)

    def test_set_online(self):
        node = Node.objects.get(key=self.key_1)
        node.online = False
        self.assertFalse(node.online)


class UptimeTestCase(TestCase):
    last_checked = datetime(2018, 1, 1)
    key_1 = "02a30a4684e915dc5b8225ad105ca2c9c2844a97982d3d0042e856670fb1285512"
    key_2 = "020907316c650dcc89629f8a1960e2309228d31718da41274f67b4c947d1006f68"
   

    def setUp(self):
        node1 = Node.objects.create(key=self.key_1, online=True, last_checked=self.last_checked)
        Uptime.objects.create(node= node1, start_time=120)
        Uptime.objects.create(node= node1, start_time=80)
        node2 = Node.objects.create(key=self.key_2, online=False, last_checked=self.last_checked)
        Uptime.objects.create(node= node2, start_time=100)

    def test_count_uptimes(self):
        expected_uptime_periods = 2
        node = Node.objects.get(key=self.key_1)
        count_periods = Uptime.objects.filter(node=node).count()
        self.assertEqual(expected_uptime_periods, count_periods)

    def test_set_start_time(self):
        expected_start_time = 30
        node = Node.objects.get(key=self.key_1)
        periods_list = Uptime.objects.filter(node=node)

        for period in periods_list:
            period.start_time = 30
            self.assertEqual(expected_start_time, period.start_time)


