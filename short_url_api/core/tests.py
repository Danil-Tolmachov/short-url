from django.test import TestCase

from core.utils import generate_short_link


class TestService(TestCase):

    def test_generate_short_link(self):
        pk = 42
        host = 'localhost:8000'

        result = generate_short_link(pk)
        expected = 'http://' + host + '/NDI='

        self.assertIsNotNone(result)
        self.assertEqual(result, expected)

    def test_link_create(self):
        pass

    def test_get_redirect_link(self):
        pass
