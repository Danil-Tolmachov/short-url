import re

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def encode_link(pk: int) -> str:
    cyphered = urlsafe_base64_encode(force_bytes(str(pk)))
    return cyphered


def decode_link(link: str) -> int:
    decoded = urlsafe_base64_decode(link)
    return int(decoded)


def validate_link(link: str):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\." + \
                   "[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    return bool(re.match(url_pattern, link))
