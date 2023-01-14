from core.utils import encode_link, validate_link, decode_link
from short_url_api.db import redis_instance, DB_COUNT
from short_url_api.settings import LINK_TIMEOUT

# receives source link
# returns short link
def set_link(request, link: str) -> str:

    if not validate_link(link):
        raise ValueError

    link_obj = DB_COUNT + 1
    redis_instance.set(link_obj, link, LINK_TIMEOUT)

    host = request.build_absolute_uri('/')
    short_link = host + encode_link(link_obj)

    return short_link


# receives cyphered(base64) pk
# returns redirect link
def get_link(encoded_pk: str) -> str:
    decoded_pk = decode_link(encoded_pk)
    source = redis_instance.get(decoded_pk)
    return source.decode()
