import deezer
import unittest
from mock import patch
from .mocked_methods import fake_urlopen

class TestResources(unittest.TestCase):

    def setUp(self):
        self.patcher = patch('deezer.client.urlopen', fake_urlopen)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_album_attributes(self):
        client = deezer.Client()
        album = client.get_album(302127)
        self.assertTrue(hasattr(album, 'title'))
        artist = album.get_artist()
        self.assertTrue(isinstance(artist, deezer.resources.Artist))
