from datetime import datetime
from django.test import TestCase
from skywire_node_checker.status_checker.models import Node, Uptime
from unittest import mock
from skywire_node_checker.status_checker.utils import autoupdate

class AutoUpdateTestCase(TestCase):

	def setUp(self):
		self.response_origin = [{"key":"02a30a4684e915dc5b8225ad105ca2c9c2844a97982d3d0042e856670fb1285512","type":"TCP","send_bytes":19182,"recv_bytes":19550,"last_ack_time":19,"start_time":125834},{"key":"020907316c650dcc89629f8a1960e2309228d31718da41274f67b4c947d1006f68","type":"TCP","send_bytes":138915,"recv_bytes":139288,"last_ack_time":59,"start_time":924086},{"key":"03b30c57928197913dae276165e03cda06e7c86ce9a50917f91bd784101256c81d","type":"TCP","send_bytes":427,"recv_bytes":797,"last_ack_time":35,"start_time":815},{"key":"020c35929e7042d03db01777b32f9a200ed4ac716d1bc99d6704c8686495a29e14","type":"TCP","send_bytes":102159,"recv_bytes":102525,"last_ack_time":47,"start_time":679067},{"key":"02f4e21fda5d6025d78cd08529a40d99a294991106718d7b97bc51503e850e7d4e","type":"TCP","send_bytes":65289,"recv_bytes":65655,"last_ack_time":52,"start_time":433252},{"key":"03b64429f80a622ee1a44922a9ebf526a432ab9d32f8aebfd86d53530656310233","type":"TCP","send_bytes":39634,"recv_bytes":39996,"last_ack_time":41,"start_time":262240},{"key":"03f9232758485c41b03fe8c5665b05ac3beb8b2f874a02fed911d8d444000e9923","type":"TCP","send_bytes":49169,"recv_bytes":49542,"last_ack_time":3,"start_time":325742},{"key":"035fd2e38eb3a785a254c0a19dc29edd82bb00a3755e9966940c9facae453398fb","type":"TCP","send_bytes":28019,"recv_bytes":28390,"last_ack_time":29,"start_time":184768},{"key":"033a54791d0b1225d29bdcb6064a0a82f75b0ba2c1d2a6c1ef592c72b426afb040","type":"TCP","send_bytes":179897,"recv_bytes":180249,"last_ack_time":15,"start_time":1197206},{"key":"02d7a852dc5d5ff3de1fbeb9bc6d1f2d58834b691566430e9b8bd486bf901ad149","type":"TCP","send_bytes":8578,"recv_bytes":8937,"last_ack_time":35,"start_time":55173},{"key":"036012c2643550c3fe12a566f7ce2e1a905904d8eb57e4591dfbc3c03692a820c3","type":"TCP","send_bytes":4291,"recv_bytes":4651,"last_ack_time":23,"start_time":26602},{"key":"0286345d9878ec84fb33fb8c6ccd6533b567ca350070e1f7c97273a00a18488581","type":"TCP","send_bytes":182786,"recv_bytes":183155,"last_ack_time":15,"start_time":1216515},{"key":"024d1332297c9b9a8358aa4dcaa4b7ecb9f39ee1535c8d01953d2172460a296b5c","type":"TCP","send_bytes":58926,"recv_bytes":59296,"last_ack_time":57,"start_time":390836},{"key":"03654695b24728feedd6c048c81acc0e79bb25599b1dbaf09e0567412ad093fcfd","type":"TCP","send_bytes":367821,"recv_bytes":368196,"last_ack_time":49,"start_time":2450052},{"key":"026891a6246c177d0a54c815231b5433fc2c227917867706de2a36e56edf84af41","type":"TCP","send_bytes":235331,"recv_bytes":235701,"last_ack_time":8,"start_time":1566848},{"key":"02f0b15e4d13e70d51252c1164b1b15fc6649f6033936c930ecbc4d531e7962d97","type":"TCP","send_bytes":50934,"recv_bytes":51298,"last_ack_time":40,"start_time":337538},{"key":"0202dbad33b94c110b66cab857b18c34f2e7f9c7a734ff35cf84fd188fca9d6c10","type":"TCP","send_bytes":30229,"recv_bytes":30609,"last_ack_time":35,"start_time":199535},{"key":"03fba33aa2b4e361d83e8d63a85548a3f51c89567ee534c136a5bbdf4038b8d63c","type":"TCP","send_bytes":42292,"recv_bytes":42653,"last_ack_time":59,"start_time":279958},{"key":"0378a3c2735e353ca601683da82d6971cb9e4be9a27427b78267981e9139ef46c9","type":"TCP","send_bytes":430820,"recv_bytes":431192,"last_ack_time":1,"start_time":2869987},{"key":"036b878999d09ac5233d0d04a2a7c86b9adac8c22241f85555475d957b27bab95a","type":"TCP","send_bytes":84671,"recv_bytes":85044,"last_ack_time":21,"start_time":562440},{"key":"038b318c764e6dcad857c2580c43ea68f597a74e37f34bba8397c9e753fe717833","type":"TCP","send_bytes":1095,"recv_bytes":1456,"last_ack_time":36,"start_time":5255}]
		self.response_key_1_offline = [{"key":"020907316c650dcc89629f8a1960e2309228d31718da41274f67b4c947d1006f68","type":"TCP","send_bytes":138915,"recv_bytes":139288,"last_ack_time":59,"start_time":924086},{"key":"03b30c57928197913dae276165e03cda06e7c86ce9a50917f91bd784101256c81d","type":"TCP","send_bytes":427,"recv_bytes":797,"last_ack_time":35,"start_time":815},{"key":"020c35929e7042d03db01777b32f9a200ed4ac716d1bc99d6704c8686495a29e14","type":"TCP","send_bytes":102159,"recv_bytes":102525,"last_ack_time":47,"start_time":679067},{"key":"02f4e21fda5d6025d78cd08529a40d99a294991106718d7b97bc51503e850e7d4e","type":"TCP","send_bytes":65289,"recv_bytes":65655,"last_ack_time":52,"start_time":433252},{"key":"03b64429f80a622ee1a44922a9ebf526a432ab9d32f8aebfd86d53530656310233","type":"TCP","send_bytes":39634,"recv_bytes":39996,"last_ack_time":41,"start_time":262240},{"key":"03f9232758485c41b03fe8c5665b05ac3beb8b2f874a02fed911d8d444000e9923","type":"TCP","send_bytes":49169,"recv_bytes":49542,"last_ack_time":3,"start_time":325742},{"key":"035fd2e38eb3a785a254c0a19dc29edd82bb00a3755e9966940c9facae453398fb","type":"TCP","send_bytes":28019,"recv_bytes":28390,"last_ack_time":29,"start_time":184768},{"key":"033a54791d0b1225d29bdcb6064a0a82f75b0ba2c1d2a6c1ef592c72b426afb040","type":"TCP","send_bytes":179897,"recv_bytes":180249,"last_ack_time":15,"start_time":1197206},{"key":"02d7a852dc5d5ff3de1fbeb9bc6d1f2d58834b691566430e9b8bd486bf901ad149","type":"TCP","send_bytes":8578,"recv_bytes":8937,"last_ack_time":35,"start_time":55173},{"key":"036012c2643550c3fe12a566f7ce2e1a905904d8eb57e4591dfbc3c03692a820c3","type":"TCP","send_bytes":4291,"recv_bytes":4651,"last_ack_time":23,"start_time":26602},{"key":"0286345d9878ec84fb33fb8c6ccd6533b567ca350070e1f7c97273a00a18488581","type":"TCP","send_bytes":182786,"recv_bytes":183155,"last_ack_time":15,"start_time":1216515},{"key":"024d1332297c9b9a8358aa4dcaa4b7ecb9f39ee1535c8d01953d2172460a296b5c","type":"TCP","send_bytes":58926,"recv_bytes":59296,"last_ack_time":57,"start_time":390836},{"key":"03654695b24728feedd6c048c81acc0e79bb25599b1dbaf09e0567412ad093fcfd","type":"TCP","send_bytes":367821,"recv_bytes":368196,"last_ack_time":49,"start_time":2450052},{"key":"026891a6246c177d0a54c815231b5433fc2c227917867706de2a36e56edf84af41","type":"TCP","send_bytes":235331,"recv_bytes":235701,"last_ack_time":8,"start_time":1566848},{"key":"02f0b15e4d13e70d51252c1164b1b15fc6649f6033936c930ecbc4d531e7962d97","type":"TCP","send_bytes":50934,"recv_bytes":51298,"last_ack_time":40,"start_time":337538},{"key":"0202dbad33b94c110b66cab857b18c34f2e7f9c7a734ff35cf84fd188fca9d6c10","type":"TCP","send_bytes":30229,"recv_bytes":30609,"last_ack_time":35,"start_time":199535},{"key":"03fba33aa2b4e361d83e8d63a85548a3f51c89567ee534c136a5bbdf4038b8d63c","type":"TCP","send_bytes":42292,"recv_bytes":42653,"last_ack_time":59,"start_time":279958},{"key":"0378a3c2735e353ca601683da82d6971cb9e4be9a27427b78267981e9139ef46c9","type":"TCP","send_bytes":430820,"recv_bytes":431192,"last_ack_time":1,"start_time":2869987},{"key":"036b878999d09ac5233d0d04a2a7c86b9adac8c22241f85555475d957b27bab95a","type":"TCP","send_bytes":84671,"recv_bytes":85044,"last_ack_time":21,"start_time":562440},{"key":"038b318c764e6dcad857c2580c43ea68f597a74e37f34bba8397c9e753fe717833","type":"TCP","send_bytes":1095,"recv_bytes":1456,"last_ack_time":36,"start_time":5255}]
		self.response_key_1_online = [{"key":"02a30a4684e915dc5b8225ad105ca2c9c2844a97982d3d0042e856670fb1285512","type":"TCP","send_bytes":19182,"recv_bytes":19550,"last_ack_time":19,"start_time":30},{"key":"020907316c650dcc89629f8a1960e2309228d31718da41274f67b4c947d1006f68","type":"TCP","send_bytes":138915,"recv_bytes":139288,"last_ack_time":59,"start_time":924086},{"key":"03b30c57928197913dae276165e03cda06e7c86ce9a50917f91bd784101256c81d","type":"TCP","send_bytes":427,"recv_bytes":797,"last_ack_time":35,"start_time":815},{"key":"020c35929e7042d03db01777b32f9a200ed4ac716d1bc99d6704c8686495a29e14","type":"TCP","send_bytes":102159,"recv_bytes":102525,"last_ack_time":47,"start_time":679067},{"key":"02f4e21fda5d6025d78cd08529a40d99a294991106718d7b97bc51503e850e7d4e","type":"TCP","send_bytes":65289,"recv_bytes":65655,"last_ack_time":52,"start_time":433252},{"key":"03b64429f80a622ee1a44922a9ebf526a432ab9d32f8aebfd86d53530656310233","type":"TCP","send_bytes":39634,"recv_bytes":39996,"last_ack_time":41,"start_time":262240},{"key":"03f9232758485c41b03fe8c5665b05ac3beb8b2f874a02fed911d8d444000e9923","type":"TCP","send_bytes":49169,"recv_bytes":49542,"last_ack_time":3,"start_time":325742},{"key":"035fd2e38eb3a785a254c0a19dc29edd82bb00a3755e9966940c9facae453398fb","type":"TCP","send_bytes":28019,"recv_bytes":28390,"last_ack_time":29,"start_time":184768},{"key":"033a54791d0b1225d29bdcb6064a0a82f75b0ba2c1d2a6c1ef592c72b426afb040","type":"TCP","send_bytes":179897,"recv_bytes":180249,"last_ack_time":15,"start_time":1197206},{"key":"02d7a852dc5d5ff3de1fbeb9bc6d1f2d58834b691566430e9b8bd486bf901ad149","type":"TCP","send_bytes":8578,"recv_bytes":8937,"last_ack_time":35,"start_time":55173},{"key":"036012c2643550c3fe12a566f7ce2e1a905904d8eb57e4591dfbc3c03692a820c3","type":"TCP","send_bytes":4291,"recv_bytes":4651,"last_ack_time":23,"start_time":26602},{"key":"0286345d9878ec84fb33fb8c6ccd6533b567ca350070e1f7c97273a00a18488581","type":"TCP","send_bytes":182786,"recv_bytes":183155,"last_ack_time":15,"start_time":1216515},{"key":"024d1332297c9b9a8358aa4dcaa4b7ecb9f39ee1535c8d01953d2172460a296b5c","type":"TCP","send_bytes":58926,"recv_bytes":59296,"last_ack_time":57,"start_time":390836},{"key":"03654695b24728feedd6c048c81acc0e79bb25599b1dbaf09e0567412ad093fcfd","type":"TCP","send_bytes":367821,"recv_bytes":368196,"last_ack_time":49,"start_time":2450052},{"key":"026891a6246c177d0a54c815231b5433fc2c227917867706de2a36e56edf84af41","type":"TCP","send_bytes":235331,"recv_bytes":235701,"last_ack_time":8,"start_time":1566848},{"key":"02f0b15e4d13e70d51252c1164b1b15fc6649f6033936c930ecbc4d531e7962d97","type":"TCP","send_bytes":50934,"recv_bytes":51298,"last_ack_time":40,"start_time":337538},{"key":"0202dbad33b94c110b66cab857b18c34f2e7f9c7a734ff35cf84fd188fca9d6c10","type":"TCP","send_bytes":30229,"recv_bytes":30609,"last_ack_time":35,"start_time":199535},{"key":"03fba33aa2b4e361d83e8d63a85548a3f51c89567ee534c136a5bbdf4038b8d63c","type":"TCP","send_bytes":42292,"recv_bytes":42653,"last_ack_time":59,"start_time":279958},{"key":"0378a3c2735e353ca601683da82d6971cb9e4be9a27427b78267981e9139ef46c9","type":"TCP","send_bytes":430820,"recv_bytes":431192,"last_ack_time":1,"start_time":2869987},{"key":"036b878999d09ac5233d0d04a2a7c86b9adac8c22241f85555475d957b27bab95a","type":"TCP","send_bytes":84671,"recv_bytes":85044,"last_ack_time":21,"start_time":562440},{"key":"038b318c764e6dcad857c2580c43ea68f597a74e37f34bba8397c9e753fe717833","type":"TCP","send_bytes":1095,"recv_bytes":1456,"last_ack_time":36,"start_time":5255}]
		self.key_1 = "02a30a4684e915dc5b8225ad105ca2c9c2844a97982d3d0042e856670fb1285512"
		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_origin):
			autoupdate()

	def test_nodes_first_load(self):
		expected_nodes_checked = 21
		expected_nodes_online =21
		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_origin):
			nodes_checked, nodes_online = autoupdate()

		self.assertEqual(expected_nodes_checked, nodes_checked)
		self.assertEqual(expected_nodes_online, nodes_online)

	def test_node_online_to_offline(self):
		expected_nodes_checked = 21
		expected_nodes_online =20
		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_key_1_offline ):
			nodes_checked, nodes_online = autoupdate()

		node = Node.objects.get(key=self.key_1)
		self.assertFalse(node.online)
		self.assertEqual(expected_nodes_checked, nodes_checked)
		self.assertEqual(expected_nodes_online, nodes_online)


	def test_node_offline_to_online(self):
		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_key_1_offline ):
			nodes_checked, nodes_online = autoupdate()

		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_key_1_online):
			nodes_checked, nodes_online = autoupdate()

		node = Node.objects.get(key=self.key_1)
		self.assertTrue(node.online)

	def test_new_uptime(self):
		expected_uptime_periods = 2
		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_key_1_offline ):
			nodes_checked, nodes_online = autoupdate()

		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_key_1_online):
			nodes_checked, nodes_online = autoupdate()

		node = Node.objects.get(key=self.key_1)
		count_periods = Uptime.objects.filter(node=node).count()

		self.assertEqual(expected_uptime_periods, count_periods)

	def test_total_uptime(self):
		expected_total_uptime = 125834 + 30
		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_key_1_offline ):
			nodes_checked, nodes_online = autoupdate()

		with mock.patch("skywire_node_checker.status_checker.utils.do_request", return_value=self.response_key_1_online):
			nodes_checked, nodes_online = autoupdate()

		node = Node.objects.get(key=self.key_1)
		periods_list = Uptime.objects.filter(node=node)

		total_uptime = 0
		for period in periods_list:
			total_uptime += period.start_time

		self.assertEqual(expected_total_uptime, total_uptime)


