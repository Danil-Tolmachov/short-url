from base64 import b64decode, b64encode


def encode_link(pk: int) -> str:
    cyphered = b64encode(str(pk).encode())
    return cyphered.decode()


def decode_link(link: str) -> int:
    decoded = b64decode(link.encode()).decode()

    if not decoded.isdigit():
        return -1

    return int(decoded)
