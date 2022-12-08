from django.test import TestCase

from core.utils import encode_link, decode_link


class TestService(TestCase):

    def test_encode_link(self):
        pk = 42

        expected = 'NDI='
        result = encode_link(pk)
        assert expected == result

    def test_decode_link(self):
        link = 'NDI='

        expected = 42
        result = decode_link(link)
        assert expected == result

        link = '12312d'

        expected = -1
        result = decode_link(link)
        assert expected == result

    def test_link_create(self):
        pass

    def test_get_redirect_link(self):
        pass
