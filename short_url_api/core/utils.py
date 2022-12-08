import binascii
import re
from base64 import b64decode, b64encode


def encode_link(pk: int) -> str:
    cyphered = b64encode(str(pk).encode())
    return cyphered.decode()


def decode_link(link: str) -> int:

    try:
        decoded = b64decode(link.encode()).decode()
    except binascii.Error:
        return -1

    if not decoded.isdigit():
        return -1

    return int(decoded)


def validate_link(link: str):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\." + \
                   "[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    return bool(re.match(url_pattern, link))
