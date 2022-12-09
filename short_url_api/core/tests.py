from django.test import TestCase, Client

from core.models import Link
from core.utils import encode_link, decode_link


class TestUtils(TestCase):

    def test_encode_link(self):
        pk = 42

        expected = 'NDI'
        result = encode_link(pk)
        assert expected == result

    def test_decode_link(self):
        link = 'NDI'

        expected = 42
        result = decode_link(link)
        print(result)
        assert expected == result


class TestServices(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_link = 'https://docs.djangoproject.com/en/4.1/topics/testing/tools/'

        # For get_source tests
        self.slug = '/MQ/'
        Link.objects.create(source_link=self.test_link)

    def test_link_create(self):
        # Successful request
        response = self.client.post('', {'link': self.test_link})
        self.assertTrue(response.status_code == 200)

        # No link provided
        self.test_link = ''
        response = self.client.post('', {'link': self.test_link})
        self.assertTrue(response.status_code == 404)

    def test_get_source_link(self):
        # Successful request
        response = self.client.get(self.slug)
        self.assertTrue(response.status_code == 200)

        # Invalid link
        self.slug = '/asdwac/'
        response = self.client.get(self.slug)
        self.assertTrue(response.status_code == 400)
