from django.test import TestCase

from core.utils import encode_link, decode_link


class TestService(TestCase):

    def test_encode_link(self):
        pk = 42
        expected = encode_link(pk)
        result = 'NDI='
        assert expected == result

    def test_decode_link(self):
        link = 'NDI='
        expected = decode_link(link)
        result = 42
        assert expected == result

    def test_link_create(self):
        pass

    def test_get_redirect_link(self):
        pass
